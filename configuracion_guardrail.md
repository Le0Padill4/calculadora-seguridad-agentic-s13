# Configuración del guardrail

El control didáctico está en `.claude/hooks/proteger_env.py`. Recibe eventos JSON con `tool_name` y `tool_input`, y devuelve 2 cuando detecta `.env` o `verificar_entorno.py`; devuelve 0 en los demás casos. El banco del profesor simuló lecturas, edición y comandos de Bash y PowerShell.

La configuración del docente es para Claude Code. Este trabajo se realizó con Codex: la prueba independiente del script por sí sola no demuestra su instalación en un agente.

Se preparó `.codex/hooks.json` para el evento `PreToolUse` y las herramientas `Bash|apply_patch`, según la documentación de Codex. En una primera sesión se solicitó `cat .env` y las pruebas: estas últimas pasaron, pero la lectura devolvió `Permission denied` mientras el archivo tenía permisos de lectura desactivados. Esa primera traza no permite atribuir el bloqueo al hook.

## Comprobación integrada posterior

En Codex CLI 0.162.1 se registró el mismo hook directamente para una sesión aislada mediante `features.hooks=true` y esta opción de configuración:

```toml
hooks.PreToolUse=[{matcher="Bash|apply_patch",hooks=[{type="command",command="python3 .claude/hooks/proteger_env.py"}]}]
```

Se usó `--dangerously-bypass-hook-trust` para esa ejecución porque se revisó el script local; no cambia la configuración global. La configuración de `.codex/hooks.json` no se cargó en la primera sesión aislada, por lo que la demostración corresponde a la configuración explícita de la sesión, no a la carga automática del proyecto.

La variable opcional `S13_HOOK_AUDIT` activa un registro local que solo guarda evento, herramienta y decisión, sin argumentos ni secretos. El registro mostró `bloquear` y `permitir`; el diagnóstico del CLI confirmó `Command blocked by PreToolUse hook: Bloqueado: recurso protegido` para `test -f .env`. La prueba se limitó a comprobar existencia, sin leer el contenido. El comando permitido ejecutó las ocho pruebas correctamente. Las trazas están en `evidencias/`.
