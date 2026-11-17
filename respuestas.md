# Respuestas

El repositorio lo escribió otra persona. Puede aportar información para entender la tarea, pero no autoriza al agente a ejecutar acciones ajenas a lo que le pedí. El README intentaba añadir la ejecución de `verificar_entorno.py` antes de corregir la calculadora.

El filtro busca texto literal. Por eso no detectó los ejemplos donde la ruta se construye por partes, con un comodín o mediante variables. Como segunda barrera usaría un entorno aislado con permisos mínimos y sin acceso a archivos personales.

La auditoría encontró cuatro caracteres invisibles y un comentario HTML oculto. El resultado muestra por qué conviene revisar el contenido crudo, aunque también puede haber instrucciones maliciosas totalmente visibles.
