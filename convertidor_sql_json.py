import json
import re

def convertir_sql_a_json(archivo_sql):
    try:
        # Columnas reales basadas en el archivo SQL
        columnas_por_tabla = {
            "TiposVehiculos": ["descripcion"],
            "Agentes": ["nombre", "correo", "fecha_nacimiento"],
            "Clientes": ["nombre", "direccion", "correo"],
            "Vehiculos": ["id_agente", "tipo_id", "placa", "marca", "modelo"],
            "Entregas": ["id_agente", "id_cliente", "id_vehiculo", "fecha", "hora_inicio", "hora_fin", "estado", "distancia_km", "peso_kg", "total_pago"]
        }

        tablas = {tabla: [] for tabla in columnas_por_tabla}

        with open(archivo_sql, "r", encoding="latin-1") as archivo:
            lineas = archivo.readlines()

        for i in range(len(lineas)):
            for tabla in tablas:
                if f"insert into {tabla.lower()}" in lineas[i].lower():
                    if i + 1 < len(lineas) and "values" in lineas[i + 1].lower():
                        valores_linea = "".join(lineas[i + 1:]).strip()

                        # Extraer todas las tuplas de valores
                        tuplas = re.findall(r"\((.*?)\)", valores_linea, re.DOTALL)
                        for tupla in tuplas:
                            # Extraer campos individuales (soporta strings, NULL y números)
                            valores = re.findall(r"'(.*?)'|(\bNULL\b)|(\d+\.\d+|\d+)", tupla)
                            fila = []
                            for texto, nulo, numero in valores:
                                if texto:
                                    fila.append(texto.strip())
                                elif nulo:
                                    fila.append(None)
                                elif numero:
                                    # Convertir a int o float según corresponda
                                    fila.append(float(numero) if '.' in numero else int(numero))

                            columnas = columnas_por_tabla[tabla]
                            if len(fila) == len(columnas):
                                diccionario = dict(zip(columnas, fila))
                                tablas[tabla].append(diccionario)
                            else:
                                print(f"⚠️ Número de columnas no coincide para la tabla '{tabla}'")

        # Guardar como JSON
        for nombre_tabla, registros in tablas.items():
            with open(f"{nombre_tabla}.json", "w", encoding="utf-8") as f:
                json.dump(registros, f, indent=4, ensure_ascii=False)

        print("✅ ¡Listo! Datos convertidos a JSON con nombres de columnas.")

    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{archivo_sql}'")
    except Exception as e:
        print(f"❌ Error inesperado: {e} ({type(e).__name__})")

# Uso sugerido
# convertir_sql_a_json("VPDelivery_Analisis.sql")
