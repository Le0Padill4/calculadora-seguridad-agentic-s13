# Configuración del guardrail

El control didáctico está en `.claude/hooks/proteger_env.py`. Recibe eventos JSON con `tool_name` y `tool_input`, y devuelve 2 cuando detecta `.env` o `verificar_entorno.py`; devuelve 0 en los demás casos. El banco del profesor simuló lecturas, edición y comandos de Bash y PowerShell.

La configuración del docente es para Claude Code. Este trabajo se realizó con Codex; no se ha verificado que Codex cargue ese hook ni se afirma que haya interceptado herramientas reales. La prueba independiente del script no demuestra su instalación en un agente. Queda pendiente comprobar un control compatible con el agente y repetir las pruebas con él activo.

Se preparó `.codex/hooks.json` para el evento `PreToolUse` y las herramientas `Bash|apply_patch`, según la documentación de Codex. En una sesión de prueba se solicitó `cat .env` y las pruebas: estas últimas pasaron, pero el intento de lectura devolvió `Permission denied` mientras el archivo tenía permisos de lectura desactivados. La traza no permite atribuir ese bloqueo al hook; la prueba integrada sigue sin demostrar que haya sido cargado.
