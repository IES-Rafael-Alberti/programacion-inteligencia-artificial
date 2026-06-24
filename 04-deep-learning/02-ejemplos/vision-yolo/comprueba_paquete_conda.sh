#!/bin/bash

# Nombre del paquete a buscar
PACKAGE_NAME=$1

# Obtener el entorno activo
ACTIVE_ENV=$(conda info --json | jq -r '.active_prefix' | awk -F '/' '{print $NF}')

# Obtener la lista de entornos Conda
ENVIRONMENTS=$(conda env list | awk '{print $1}' | tail -n +3)

echo "Buscando el paquete '$PACKAGE_NAME' en los entornos Conda..."

# Revisar el entorno activo
echo "🔍 Revisando el entorno activo: $ACTIVE_ENV"
if conda list | grep -q "^$PACKAGE_NAME "; then
    echo "✅ Encontrado en el entorno activo: $ACTIVE_ENV"
else
    echo "❌ No encontrado en el entorno activo: $ACTIVE_ENV"
fi

# Revisar otros entornos
for ENV in $ENVIRONMENTS; do
    if [ "$ENV" != "$ACTIVE_ENV" ]; then
        if conda list -n $ENV | grep -q "^$PACKAGE_NAME "; then
            echo "✅ Encontrado en el entorno: $ENV"
        else
            echo "❌ No encontrado en el entorno: $ENV"
        fi
    fi
done