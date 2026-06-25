# asistente_mcp.py
import gradio as gr
import wikipedia
import sqlite3
import requests
from datetime import datetime
from transformers import pipeline

# === Base de datos SQLite ===
conn = sqlite3.connect("mcp_contexto.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS historial (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        contexto TEXT,
        respuesta TEXT,
        fuente TEXT,
        timestamp TEXT
    )
""")
conn.commit()

# === Herramientas externas ===
def obtener_contexto_wikipedia(pregunta):
    try:
        return wikipedia.summary(pregunta, sentences=2, auto_suggest=True), "Wikipedia"
    except Exception as e:
        return f"Error en Wikipedia: {e}", "Wikipedia"

def obtener_clima():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=40.4&longitude=-3.7&current_weather=true"
        r = requests.get(url).json()
        datos = r["current_weather"]
        return f"Temperatura: {datos['temperature']}°C, Viento: {datos['windspeed']} km/h", "Open-Meteo"
    except Exception as e:
        return f"Error en API clima: {e}", "Open-Meteo"

# === Modelo ===
qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

# === Lógica MCP ===
def asistente(pregunta, usar_api):
    contexto, fuente = obtener_clima() if usar_api else obtener_contexto_wikipedia(pregunta)
    resultado = qa(question=pregunta, context=contexto)
    respuesta = resultado["answer"]

    cursor.execute("INSERT INTO historial (pregunta, contexto, respuesta, fuente, timestamp) VALUES (?, ?, ?, ?, ?)",
                   (pregunta, contexto, respuesta, fuente, datetime.now().isoformat()))
    conn.commit()
    return respuesta

def ver_historial():
    cursor.execute("SELECT pregunta, fuente, respuesta, timestamp FROM historial ORDER BY id DESC LIMIT 5")
    filas = cursor.fetchall()
    if not filas:
        return "Historial vacío."
    return "\n\n".join([f"{t[:19]} | {f} | {p} → {r}" for p, f, r, t in filas])

# === Interfaz Gradio ===
with gr.Blocks() as app:
    gr.Markdown("# Asistente IA con Contexto (MCP)")
    pregunta = gr.Textbox(label="Pregunta")
    usar_api = gr.Checkbox(label="Usar API del clima en lugar de Wikipedia")
    salida = gr.Textbox(label="Respuesta")
    historial = gr.Textbox(label="Historial")

    gr.Button("Enviar").click(asistente, inputs=[pregunta, usar_api], outputs=salida)
    gr.Button("Ver historial").click(ver_historial, outputs=historial)

app.launch()
