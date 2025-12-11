import json
import pandas as pd
import re
import os

# Traemos la función desde el otro archivo
from convertidor_sql_json import convertir_sql_a_json
from Analisis_datos import entregas_por_agente, peso_promedio_por_agente, total_pago_por_agente, entregas_por_dia
from carga_datos import cargar_datos

entregas, agentes = cargar_datos()



def main():

    while True:
        print("\n📊 MENÚ DE ANÁLISIS DE VPDelivery")
        print("1. Converir SQL a JSON")
        print("2. Ver entregas por agente")
        print("3. Ver peso promedio por agente")
        print("4. Ver total entregado por agente")
        print("5. Ver entregas por día de la semana")
        print("6. Ver gráfico de entregas por agente")
        print("0. Salir")

        opcion = input("Selecciona una opción (0-6): ")
        if opcion == "1":
            archivo_sql = "C:/Users/Joss/Documents/Analisis de Datos/vpdelivery_proyecto/Proyecto_Analisis_de_Datos/VPDelivery_Analisis.sql"
            convertir_sql_a_json(archivo_sql)
        elif opcion == "2":
            conteo = entregas_por_agente(entregas, agentes)
        elif opcion == "3":
            total_pago_por_agente(entregas, agentes)
        elif opcion == "4":
            peso_promedio_por_agente(entregas, agentes)
        elif opcion == "5":
            total_pago_por_agente(entregas, agentes)
        elif opcion == "6":
            entregas_por_dia(entregas)
        elif opcion == "5":
            try:
                conteo  # usar el conteo generado en opción 1
            except NameError:
                conteo = entregas_por_agente(entregas, agentes)
            graficar_entregas_por_agente(conteo, agentes)
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()