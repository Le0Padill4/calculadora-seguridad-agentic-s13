"""Control didáctico de eventos PreToolUse; no sustituye un sandbox."""
import json
import re
import sys

try:
    evento = json.load(sys.stdin)
    contenido = json.dumps(evento.get("tool_input", {}), ensure_ascii=False)
except (ValueError, AttributeError):
    print("Evento inválido: operación bloqueada", file=sys.stderr)
    sys.exit(2)

if re.search(r"\.env\b|verificar_entorno\.py", contenido, re.IGNORECASE):
    print("Bloqueado: recurso protegido", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
