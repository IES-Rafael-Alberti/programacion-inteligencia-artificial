#!/usr/bin/env zsh

set -euo pipefail

echo "MEMORIAS GUARDADAS"
echo "=================="
if [[ -d "$HOME/.codex/memories" ]]; then
  ls -1 "$HOME/.codex/memories" 2>/dev/null || true
else
  echo "No existe ~/.codex/memories"
fi

echo
echo "ULTIMAS SESIONES"
echo "================"
if [[ -d "$HOME/.codex/sessions" ]]; then
  find "$HOME/.codex/sessions" -type f -printf '%TY-%Tm-%Td %TH:%TM %p\n' | sort | tail -n 20
else
  echo "No existe ~/.codex/sessions"
fi

echo
echo "USO"
echo "==="
echo "Para ver una memoria concreta:"
echo "  cat ~/.codex/memories/NOMBRE.md"
echo
echo "Para ver una sesion concreta:"
echo "  less RUTA_DE_LA_SESION"
