# mini_tracker (versión funcional)

Este paquete implementa un sistema sencillo de seguimiento de tareas utilizando **funciones** y una **variable global** para almacenar el tiempo acumulado.

## Uso

```python
from mini_tracker import iniciar_tarea, detener_tarea, consultar_total

iniciar_tarea("Escribir informe")
detener_tarea(2.5)

iniciar_tarea("Revisar código")
detener_tarea(1.5)

print(f"Tiempo total acumulado: {consultar_total()} horas")
Explica que se usa una variable global tiempo_total_acumulado y que las funciones modifican ese estado. Describe cómo se usa el paquete y muestra un ejemplo de flujo de trabajo.

Flujo de trabajo
- Se inicia una tarea con iniciar_tarea.
- Se detiene la tarea indicando las horas trabajadas con detener_tarea.
- El tiempo se acumula en una variable global compartida por todas las funciones.
- Se consulta el total con consultar_total.
Nota
El uso de estado global facilita la implementación, pero limita la flexibilidad cuando se requieren múltiples seguimientos independientes.


Como ejecutar el archivo.

1.Abrimos la terminal en la carpeta raiz del projecto y copeamos :
cd "C:\Users\Rafa Morales\Documents\Ejercicio U\mini_tracker_task"

2. ejecutamos python main.py 
