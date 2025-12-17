import csv
import pandas as pd
import re


# Traemos la función desde el otro archivo

from convertir_sql_csv import convertir_sql_a_csv  # Asegúrate de que esta función esté definida en un archivo llamado convertir_sql.py
from carga_datos import cargar_datos
from Analisis_datos import (
    agentes_mas_eficientes_por_peso,
    vehiculo_mas_usado,cliente_top_entregas,
    peso_promedio_por_tipo_vehiculo,hora_mas_activa
    
)

def main():

    try:
        archivo_sql = "C:/Users/Joss/Documents/Analisis de Datos/vpdelivery_proyecto/Proyecto_Analisis_de_Datos/VPDelivery_Analisis1.sql" 
        convertir_sql_a_csv(archivo_sql)
        
        while True:
            
            print("\n📊 MENÚ DE ANÁLISIS DE VPDelivery")
            print("1. Carga de datos")
            print("2. Ver agentes más eficientes")
            print("3. Ver vehículos más usados")
            print("4. Ver clientes top de entregas")
            print("5. Ver peso promedio por tipo de vehículo")
            print("6. Ver hora más activa")
            print("0. Salir")
            
            opcion = input("Selecciona una opción (0-9): ")
            if opcion == "1":
                print("📥 Cargando datos iniciales...")
                agentes, clientes, entregas, vehiculos, tiposVehiculos = cargar_datos()
                if agentes is None:
                    return
                print("✅ Carga datos Exitosa...")
            
            elif opcion == "2":
                agentes_mas_eficientes_por_peso(entregas, agentes)
            elif opcion == "3":
                vehiculo_mas_usado(entregas, vehiculos,tiposVehiculos)
            elif opcion == "4":
                cliente_top_entregas(entregas, clientes)
            elif opcion == "5":
                peso_promedio_por_tipo_vehiculo(entregas, vehiculos, tiposVehiculos)
            
            elif opcion == "6":
                hora_mas_activa(entregas)
        
        
            elif opcion == "0":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("⚠️ Opción no válida. Intenta de nuevo.")
    except Exception as e:
            print(f"❌ Ocurrió un error en el programa: {e}")
            
if __name__ == "__main__":
    main()
