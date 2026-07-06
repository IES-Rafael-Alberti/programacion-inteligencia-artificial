"""
Script de Métricas para Comparativa de Modelos
=============================================

Usage:
    python metricas.py --modelo transformer --epocas 300 --d_model 64
"""

import argparse
import time
import torch
import torch.nn as nn
from pathlib import Path
import json
from datetime import datetime


class MetricsCollector:
    """Recopila métricas durante entrenamiento e inferencia"""
    
    def __init__(self, nombre_modelo, tarea):
        self.nombre = nombre_modelo
        self.tarea = tarea
        self.metrics = {
            "modelo": nombre_modelo,
            "tarea": tarea,
            "timestamp": datetime.now().isoformat(),
            "entrenamiento": {},
            "inferencia": {},
            "recursos": {},
        }
        self.epoch_times = []
        self.inferencia_times = []
    
    def add_train_epoch(self, epoch, loss, lr=None):
        """Registra métricas de una época"""
        if "epochs" not in self.metrics["entrenamiento"]:
            self.metrics["entrenamiento"]["epochs"] = []
        
        data = {
            "epoch": epoch,
            "loss": loss,
        }
        if lr:
            data["lr"] = lr
        self.metrics["entrenamiento"]["epochs"].append(data)
    
    def add_epoch_time(self, seconds):
        """Registra tiempo de una época"""
        self.epoch_times.append(seconds)
        self.metrics["entrenamiento"]["tiempo_por_epoca_s"] = self.epoch_times.copy()
    
    def add_inferencia_time(self, seconds):
        """Registra tiempo de una predicción"""
        self.inferencia_times.append(seconds)
        self.metrics["inferencia"]["tiempos"] = self.inferencia_times.copy()
    
    def finalize(self, model):
        """Calcula métricas finales"""
        # Recursos
        self.metrics["recursos"]["parametros"] = sum(p.numel() for p in model.parameters())
        self.metrics["recursos"]["parametros_entrenables"] = sum(
            p.numel() for p in model.parameters() if p.requires_grad
        )
        
        # Tamaño del modelo
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.pt', delete=False) as f:
            torch.save(model.state_dict(), f.name)
            size_mb = Path(f.name).stat().st_size / (1024 * 1024)
            Path(f.name).unlink()
        self.metrics["recursos"]["tamano_mb"] = size_mb
        
        # Tiempos totales
        if self.epoch_times:
            self.metrics["entrenamiento"]["tiempo_total_s"] = sum(self.epoch_times)
            self.metrics["entrenamiento"]["tiempo_promedio_epoca_s"] = sum(self.epoch_times) / len(self.epoch_times)
        
        if self.inferencia_times:
            self.metrics["inferencia"]["tiempo_promedio_ms"] = (sum(self.inferencia_times) / len(self.inferencia_times)) * 1000
            self.metrics["inferencia"]["tiempo_total_s"] = sum(self.inferencia_times)
        
        # Mejor loss
        if self.metrics["entrenamiento"]["epochs"]:
            losses = [e["loss"] for e in self.metrics["entrenamiento"]["epochs"]]
            self.metrics["entrenamiento"]["loss_final"] = losses[-1]
            self.metrics["entrenamiento"]["loss_minimo"] = min(losses)
        
        return self.metrics
    
    def save(self, path):
        """Guarda métricas a JSON"""
        with open(path, 'w') as f:
            json.dump(self.metrics, f, indent=2)
        print(f"Métricas guardadas en {path}")
    
    def print_summary(self):
        """Imprime resumen de métricas"""
        print(f"\n{'='*50}")
        print(f"MÉTRICAS: {self.nombre}")
        print(f"{'='*50}")
        
        if "tiempo_total_s" in self.metrics["entrenamiento"]:
            print(f"Tiempo entrenamiento: {self.metrics['entrenamiento']['tiempo_total_s']:.2f}s")
        
        if "loss_final" in self.metrics["entrenamiento"]:
            print(f"Loss final: {self.metrics['entrenamiento']['loss_final']:.4f}")
        
        print(f"Parámetros: {self.metrics['recursos']['parametros']:,}")
        print(f"Tamaño: {self.metrics['recursos']['tamano_mb']:.2f} MB")
        
        if "tiempo_promedio_ms" in self.metrics["inferencia"]:
            print(f"Tiempo inferencia: {self.metrics['inferencia']['tiempo_promedio_ms']:.2f}ms")
        
        print(f"{'='*50}\n")


def measure_inferencia_time(model, dataloader, device, n_samples=50):
    """Mide tiempo de inferencia"""
    model.eval()
    times = []
    
    with torch.no_grad():
        for i, batch in enumerate(dataloader):
            if i >= n_samples:
                break
            
            if isinstance(batch, tuple):
                x = batch[0].to(device)
            else:
                x = batch.to(device)
            
            start = time.time()
            _ = model(x)
            end = time.time()
            
            times.append(end - start)
    
    return times


def compare_models_results(resultados_list):
    """
    Compara resultados de múltiples modelos
    
    Args:
        resultados_list: lista de diccionarios con métricas de cada modelo
    """
    print("\n" + "="*70)
    print("COMPARATIVA DE MODELOS")
    print("="*70)
    
    headers = ["Modelo", "Loss Final", "Tiempo (s)", "Params", "Tamaño (MB)", "Inf. (ms)"]
    print(f"\n{headers[0]:<15} | {headers[1]:<12} | {headers[2]:<10} | {headers[3]:<12} | {headers[4]:<12} | {headers[5]:<10}")
    print("-"*70)
    
    for r in resultados_list:
        modelo = r["modelo"]
        loss = r.get("entrenamiento", {}).get("loss_final", "N/A")
        tiempo = r.get("entrenamiento", {}).get("tiempo_total_s", "N/A")
        params = r.get("recursos", {}).get("parametros", "N/A")
        size = r.get("recursos", {}).get("tamano_mb", "N/A")
        inf_time = r.get("inferencia", {}).get("tiempo_promedio_ms", "N/A")
        
        if isinstance(loss, float):
            loss = f"{loss:.4f}"
        if isinstance(tiempo, float):
            tiempo = f"{tiempo:.2f}"
        if isinstance(params, int):
            params = f"{params:,}"
        if isinstance(size, float):
            size = f"{size:.2f}"
        if isinstance(inf_time, float):
            inf_time = f"{inf_time:.2f}"
        
        print(f"{modelo:<15} | {loss:<12} | {tiempo:<10} | {params:<12} | {size:<12} | {inf_time:<10}")
    
    print("-"*70 + "\n")


def plot_loss_curves(resultados_list, save_path="comparativa_loss.png"):
    """Genera gráfico de curvas de pérdida"""
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    for i, r in enumerate(resultados_list):
        nombre = r["modelo"]
        epochs_data = r.get("entrenamiento", {}).get("epochs", [])
        
        if epochs_data:
            epochs = [e["epoch"] for e in epochs_data]
            losses = [e["loss"] for e in epochs_data]
            plt.plot(epochs, losses, label=nombre, color=colors[i % len(colors)], linewidth=2)
    
    plt.xlabel("Época")
    plt.ylabel("Loss (Cross-Entropy)")
    plt.title("Comparativa de Convergencia")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"Gráfico guardado en {save_path}")
    plt.close()


def plot_comparison_bars(resultados_list, metric, title, save_path):
    """Genera gráfico de barras comparativo"""
    import matplotlib.pyplot as plt
    
    modelos = [r["modelo"] for r in resultados_list]
    valores = []
    
    for r in resultados_list:
        if metric == "loss":
            valores.append(r.get("entrenamiento", {}).get("loss_final", 0))
        elif metric == "tiempo":
            valores.append(r.get("entrenamiento", {}).get("tiempo_total_s", 0))
        elif metric == "params":
            valores.append(r.get("recursos", {}).get("parametros", 0) / 1000)
        elif metric == "size":
            valores.append(r.get("recursos", {}).get("tamano_mb", 0))
        elif metric == "inferencia":
            valores.append(r.get("inferencia", {}).get("tiempo_promedio_ms", 0))
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(modelos, valores, color=colors[:len(modelos)])
    
    plt.title(title)
    plt.ylabel(metric)
    plt.grid(True, alpha=0.3, axis='y')
    
    for bar, val in zip(bars, valores):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.2f}',
                ha='center', va='bottom')
    
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"Gráfico guardado en {save_path}")
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Recopila métricas de modelos")
    parser.add_argument("--modelo", type=str, default="test", help="Nombre del modelo")
    parser.add_argument("--tarea", type=str, default="test", help="Nombre de la tarea")
    parser.add_argument("--output", type=str, default="metricas.json", help="Fichero de salida")
    
    args = parser.parse_args()
    
    collector = MetricsCollector(args.modelo, args.tarea)
    
    # Ejemplo de uso (reemplazar con tu entrenamiento real)
    print(f"Recopilando métricas para {args.modelo}...")
    print("Usa esta clase en tu código de entrenamiento:")
    print("""
    collector = MetricsCollector("mi_modelo", "traduccion")
    
    for epoch in range(epochs):
        start = time.time()
        # tu training loop
        loss = train_step(...)
        end = time.time()
        
        collector.add_train_epoch(epoch, loss)
        collector.add_epoch_time(end - start)
    
    collector.add_inferencia_time(inferencia_time)
    collector.finalize(model)
    collector.save("metricas.json")
    collector.print_summary()
    """)


if __name__ == "__main__":
    main()
