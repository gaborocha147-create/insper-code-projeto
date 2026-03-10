#!/usr/bin/env python3
"""
Serves the project directory (static site) at http://localhost:8000
Usage:
    python servidor.py [--port PORT] [--bind HOST]

This uses only the Python standard library (http.server) so no extra packages are required.
"""

import http.server
import socketserver
import argparse
import os
import sys

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    # avoid noisy logs; override if you want logging
    def log_message(self, format, *args):
        pass


def main():
    parser = argparse.ArgumentParser(description="Servir site estático na pasta do projeto")
    parser.add_argument('--port', '-p', type=int, default=8000, help='Porta para servir (padrão: 8000)')
    parser.add_argument('--bind', '-b', default='127.0.0.1', help='Endereço para bind (padrão: 127.0.0.1)')
    args = parser.parse_args()

    # Serve files from the directory where this script lives (project root)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    handler_class = QuietHandler
    try:
        with socketserver.TCPServer((args.bind, args.port), handler_class) as httpd:
            print(f"Servindo em http://{args.bind}:{args.port}/ (Ctrl+C para parar)")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nInterrompido pelo usuário, encerrando servidor.')
    except OSError as e:
        print('Erro ao iniciar o servidor:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
