# main.py
from mini_tracker import iniciar_tarea, detener_tarea, consultar_total

iniciar_tarea("Escribir informe")
detener_tarea(2.5)

iniciar_tarea("Revisar código")
detener_tarea(1.5)

print(f"Tiempo total acumulado: {consultar_total()} horas")