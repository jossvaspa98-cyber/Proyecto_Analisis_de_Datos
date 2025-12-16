import csv
import pandas as pd
import re


# Traemos la función desde el otro archivo

from convertir_sql_csv import convertir_sql_a_csv  # Asegúrate de que esta función esté definida en un archivo llamado convertir_sql.py
from carga_datos import cargar_datos
from Analisis_datos import (
    entregas_por_agente,
    entregas_por_hora,
    distribucion_peso,
    total_entregado_por_tipo_vehiculo,
    top_clientes_con_mas_entregas,
    vehiculo_mas_eficiente,
    ingresos_totales_por_cliente,
)




def main():


    try:
        archivo_sql = "C:/Users/Joss/Documents/Analisis de Datos/vpdelivery_proyecto/Proyecto_Analisis_de_Datos/VPDelivery_Analisis1.sql" 
        convertir_sql_a_csv(archivo_sql)

        while True:
            print("\n📊 MENÚ DE ANÁLISIS DE VPDelivery")
            print("1. Carga de datos")
            print("2. Ver entregas por agente")
            print("3. Ver entregas por hora")
            print("4. Ver distribución de peso")
            print("5. Ver total entregado por tipo vehículo")
            print("6. Ver top clientes con más entregas")
            print("7. Ver vehículo más eficiente")
            print("8. Ver ingresos totales por cliente")
            print("0. Salir")


            opcion = input("Selecciona una opción (0-9): ")
            if opcion == "1":
                print("📥 Cargando datos iniciales...")
                agentes, clientes, entregas, vehiculos, tipos_vehiculos = cargar_datos()
                if agentes is None:
                    return
                print("Carga datos Exitosa...")
            
            elif opcion == "2":
                entregas_por_agente(entregas, agentes)

            elif opcion == "3":
                entregas_por_hora(entregas)

            elif opcion == "4":
                distribucion_peso(entregas)

            elif opcion == "5":
                total_entregado_por_tipo_vehiculo(entregas,vehiculos,tipos_vehiculos)
                
            elif opcion == "6":
                top_clientes_con_mas_entregas(entregas, clientes)
                
            elif opcion == "7": 
                vehiculo_mas_eficiente(entregas, vehiculos)
                
            elif opcion == "8":
                
                ingresos_totales_por_cliente(entregas, clientes)

            elif opcion == "0":
                print("👋 ¡Hasta luego!")
                break

            else:
                print("⚠️ Opción no válida. Intenta de nuevo.")
    except Exception as e:
            print(f"❌ Ocurrió un error en el programa: {e}")
            
if __name__ == "__main__":
    main()
