
import csv
import pandas as pd
import re
import matplotlib.pyplot as plt


# Traemos la función desde el otro archivo
from convertir_sql_csv import convertir_sql_a_csv  
from carga_datos import cargar_datos
from Analisis_datos import (
    analizar_ventas_por_periodo,vehiculo_mas_usado,
    cliente_top_entregas, analizar_eficiencia_por_agente,
    analizar_tipo_entregas,analizar_horas_pico
)

def main():
    #Iniciamos un bloque try para capturar errores inesperados que podrían ocurrir durante la ejecución del programa.
    try:
        #definimos la ruta del archivo SQL que contiene todos los datos que se van a convertir a CSV.
        archivo_sql = "C:/Users/Joss/Documents/Analisis de Datos/vpdelivery_proyecto/Proyecto_Analisis_de_Datos/VPDelivery_Analisis1.sql" 
        #llamomos a la función que convierte el contenido del archivo SQL en archivos .csv
        convertir_sql_a_csv(archivo_sql)
        
        #iniciamos un bucle infinito while True que mantiene el menú activo hasta que el usuario decida salir.
        while True:
            
            #Imprimimos un título visual para el menú de opciones.
            print("\n📊 MENÚ DE ANÁLISIS DE VPDelivery")
            print("1. Carga de datos")
            print("2. Ver agentes más eficientes")
            print("3. Ver vehículos más usados")
            print("4. Ver clientes top de entregas")
            print("5. Ver peso promedio por tipo de vehículo")
            print("6. Ver hora más activa")
            print("7. Ver Vehiculo más eficiente por kilometro")
            print("0. Salir")
            
            #Muestramos las diferentes opciones disponibles para análisis en la aplicación.
            #le pedimos al usuario que escriba una opción del menú.
            opcion = input("Selecciona una opción (0-9): ")
            if opcion == "1":
                #Llamamos a la función cargar_datos() que lee los archivos CSV y devuelve los DataFrames con los datos.
                # Se guardan en variables para usarlos más adelante.
                print("📥 Cargando datos iniciales...")
                agentes, clientes, entregas, vehiculos, tiposVehiculos = cargar_datos()
                #Si por alguna razón no se pudo cargar la tabla de agentes (error o archivo vacío), se detiene el programa.
                if agentes is None:
                    return
                print("✅ Carga datos Exitosa...")
                #Si el usuario elige 2, se realiza un análisis de ventas totales usando la función analizar_ventas_por_periodo.
            elif opcion == "2":
                analizar_ventas_por_periodo(entregas, fecha_inicio= None, fecha_fin=None)
                #Si elige 3, se analiza qué vehículos han sido los más utilizados en las entregas.
            elif opcion == "3":
                vehiculo_mas_usado(entregas, vehiculos, tiposVehiculos)
                #Si elige 4, se analiza qué clientes han recibido más entregas.
            elif opcion == "4":
                cliente_top_entregas(entregas, clientes)
                #Si elige 5, se analiza qué agentes son más eficientes (tiempo/km) 
            elif opcion == "5":
                analizar_eficiencia_por_agente(entregas, agentes)
                #Si elige 6, se analiza el estado de las entregas
            elif opcion == "6":
                analizar_tipo_entregas(entregas)
                #Si elige 7, se analizan las horas del día con más actividad de entregas
            elif opcion == "7":
                analizar_horas_pico(entregas)
                #Si elige 0, el programa se despide y sale del bucle para finalizar la ejecución.
            elif opcion == "0":
                #
                print("👋 ¡Hasta luego!")
                break
            else:
                #Si el usuario escribe algo que no está en el menú, muestra un mensaje de advertencia.
                print("⚠️ Opción no válida. Intenta de nuevo.")
                #Si ocurre cualquier error inesperado durante la ejecución del programa, se muestra el mensaje de error sin que el sistema se caiga.
    except Exception as e:
            print(f"❌ Ocurrió un error en el programa: {e}")
            
#Esta línea indica que si el archivo se ejecuta directamente, se llamará a la función main() para iniciar el programa.
#Es la forma estándar en Python de iniciar un programa principal.            
if __name__ == "__main__":
    main()
