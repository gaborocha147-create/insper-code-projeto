# insper-code-projeto
Projeto para Insper Code

Instruções rápidas para rodar o site estático localmente.

1. Criar e ativar o ambiente virtual (macOS / zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

2. Rodar o servidor local (script incluído `servidor.py`):

```bash
# dentro do diretório do projeto
python servidor.py          # serve em http://127.0.0.1:8000
# ou mudar porta
python servidor.py --port 9000
```

3. Alternativa rápida (sem venv):

```bash
python3 -m http.server 8000
```

Observações:
- O arquivo `.gitignore` já ignora a pasta `.venv` e caches.
- Para acessar na rede local rode: `python servidor.py --bind 0.0.0.0`

Arquivos úteis criados:
- `servidor.py` — servidor Python simples que serve arquivos estáticos.
- `run_server.sh` — script para ativar `.venv` (se existir) e rodar o servidor.
- `.venv/` — ambiente virtual (não comitado, está no .gitignore).
 
Template helper
---------------

Coloque o logo principal em `images/logo/logo-square.png` (ou `svg`) — anexei um arquivo de logo, você pode sobrescrever.

Para gerar páginas que usam o `global.html` (template base):

```bash
# exemplo: gere uma versão templated de equipe.html em generated/equipe.html
python tools/apply_template.py equipe.html generated/equipe.html

# abra em um navegador para checar
python -m http.server 8000 --directory generated
```

Se preferir aplicar o template diretamente às páginas em raiz, posso automatizar isso também.
# insper-code-projeto
Projeto para Insper Code
