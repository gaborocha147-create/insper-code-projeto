#!/usr/bin/env bash
# Script simples para ativar .venv (se existir) e rodar o servidor
set -e
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi
python servidor.py "$@"
