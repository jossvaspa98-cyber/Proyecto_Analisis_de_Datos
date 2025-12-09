import json
import pandas as pd
import re # Esto sirve para buscar texto dentro de otras cadenas más fácilmente


#------------------------------------------------------------
#CREACIÓN DE LA FUNCIÓN
#------------------------------------------------------------

def convertir_sql_a_json(archivo_sql):

    try: 
            # Abrimos el archivo SQL para leerlo (como si abrieras un cuaderno)
            archivo = open(archivo_sql, "r", encoding="latin-1")
            # Guardamos todo el contenido del archivo en una sola variable tipo texto
            texto = archivo.read()
            # Cerramos el archivo porque ya no lo necesitamos abierto
            archivo.close()
            # Separamos el texto en líneas (como cortar el texto en pedacitos por cada ENTER)
            lineas = texto.split("\n")
            # Volvemos a abrir el archivo, pero esta vez lo leemos línea por línea
            # Esto ayuda a buscar más fácilmente los INSERT que vienen uno debajo del otro
            with open(archivo_sql, "r", encoding="latin-1") as archivo:
                lineas = archivo.readlines()
            # ----------------------------------------------------------------------------------
            # CREAR UN LUGAR DONDE GUARDAR LOS DATOS
            # ------------------------------------------------------------
            # Creamos un diccionario donde cada "llave" es una tabla,
            # y cada una tendrá una lista donde vamos a guardar sus datos.
            tablas = {
                "clientes": [],
                "agentes": [],
                "entregas": [],
                "vehiculos": [],
                "tipos_vehiculos": [],
                "provincias": [],
                "cantones": [],
                "distritos": []
            }
            # ------------------------------------------------------------
            #BUSCAR LÍNEAS QUE CONTIENEN INSERTS
            # ------------------------------------------------------------
            # Recorremos todas las líneas del archivo SQL una por una
            for i in range(len(lineas)):
                # Revisamos cada una de las tablas que queremos extraer
                for tabla in tablas:
                    # Si la línea actual tiene algo como "insert into clientes"
                    # entonces significa que aquí empieza un registro nuevo
                    if f"insert into {tabla}" in lineas[i].lower():
                        # La línea siguiente normalmente tiene los valores
                        if i + 1 < len(lineas) and "values" in lineas[i + 1].lower():
                            # Tomamos la línea que tiene los valores (los datos que queremos guardar)
                            valores_linea = lineas[i + 1].strip()
                            # Esta línea usa una expresión (regex)
                            # para buscar:
                            # - palabras entre comillas como 'Juan'
                            # - números como 25
                            valores = re.findall(r"'(.*?)'|(\d+)", valores_linea)
                            # Aquí guardaremos cada fila encontrada
                            fila = []
                            # Revisamos cada valor que encontramos
                            for texto, numero in valores:
                                # Si encontramos texto entre comillas, lo guardamos
                                if texto:
                                    fila.append(texto.strip())
                                # Si encontramos un número, también lo guardamos
                                elif numero:
                                    fila.append(numero.strip())
                                    
                            # Guardamos la fila completa dentro de la tabla correspondiente
                            tablas[tabla].append(fila)
                            
            # ------------------------------------------------------------
            # GUARDAR DATOS EN ARCHIVOS json
            # ------------------------------------------------------------
            # Para cada tabla y los datos que tiene
            for nombre_tabla, datos in tablas.items():
                # Creamos un archivo json con el nombre de la tabla
                with open(f"{nombre_tabla}.json", "w", encoding="utf-8") as f:
                    # Guardamos los datos de la tabla dentro del archivo
                    json.dump(datos, f, indent=4, ensure_ascii=False)

                # Mensaje que indica que todo el proceso ha terminado
            print("\n ¡Listo! Todas las tablas han sido convertidas a JSON.")

    except FileNotFoundError:
        print(f" Error: No se encontró el archivo '{archivo_sql}'")
        print("   Verifica que el nombre y la ruta sean correctos.")
        return False
    
    # Si hay problemas al leer el archivo
    except IOError as error:
        print(f" Error al leer el archivo: {error}")
        return False
    
    # Si hay cualquier otro error
    except Exception as error:
        print(f" Ocurrió un error inesperado:")
        print(f"   {error}")
        return False

    