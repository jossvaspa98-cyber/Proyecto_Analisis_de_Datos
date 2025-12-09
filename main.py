import json
import pandas as pd
import re
import os

# Traemos la función desde el otro archivo
from convertidor_sql_json import convertir_sql_a_json
from limpieza_datos import limpieza_datos
from Analisis_datos import analisis_entregas_por_agente

# Esta es la ruta donde está guardado el archivo SQL
archivo_sql = "C:/Users/Joss/Documents/Analisis de Datos/vpdelivery_proyecto/Proyecto_Analisis_de_Datos/BD_VPDELIVERY_PROYECTO.sql"

# Aquí llamamos la función para que haga todo el trabajo
# leer el SQL, extraer los datos, crear los json.
convertir_sql_a_json(archivo_sql)

# Llamamos a la función limpieza_datos()
# El resultado (las 8 tablas) se guarda en la variable resultado
resultado = limpieza_datos()

# Verificamos si resultado no es None (es decir, si la limpieza fue exitosa)
if resultado is not None:
    # Si todo está bien, sacamos cada DataFrame 
    # Es como sacar cosas de una caja y ponerles nombre a cada una
    df_clientes, df_agentes, df_entregas, df_vehiculos, df_tipos_vehiculos, df_provincias, df_cantones, df_distritos = resultado
    
    print(f"\n Registros por tabla:")
    print(f"Clientes: {len(df_clientes)}")
    print(f"Agentes: {len(df_agentes)}")
    print(f"Entregas: {len(df_entregas)}")
    print(f"Vehículos: {len(df_vehiculos)}")
    print(f"Tipos vehículos: {len(df_tipos_vehiculos)}")
    print(f"Provincias: {len(df_provincias)}")
    print(f"Cantones: {len(df_cantones)}")
    print(f"Distritos: {len(df_distritos)}")
else:
    print("No se pudieron cargar los datos.")


analisis_entregas_por_agente()
