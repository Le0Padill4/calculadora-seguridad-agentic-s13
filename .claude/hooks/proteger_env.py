"""Control didáctico de eventos PreToolUse; no sustituye un sandbox."""
import json
import os
import re
import sys

try:
    evento = json.load(sys.stdin)
    contenido = json.dumps(evento.get("tool_input", {}), ensure_ascii=False)
except (ValueError, AttributeError):
    print("Evento inválido: operación bloqueada", file=sys.stderr)
    sys.exit(2)

bloqueado = bool(re.search(r"\.env\b|verificar_entorno\.py", contenido, re.IGNORECASE))
registro = os.environ.get("S13_HOOK_AUDIT")
if registro:
    with open(registro, "a", encoding="utf-8") as archivo:
        archivo.write(json.dumps({"evento": evento.get("hook_event_name"), "herramienta": evento.get("tool_name"), "decision": "bloquear" if bloqueado else "permitir"}) + "\n")

if bloqueado:
    print("Bloqueado: recurso protegido", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
