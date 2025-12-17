import pandas as pd
import re

def convertir_sql_a_csv(archivo_sql):
    # Abrimos un bloque try para manejar posibles errores durante el proceso.
    try:
        # Abrir y leer el archivo SQL
        # Usamos open para abrir el archivo en modo lectura y una codificación estándar (`utf-8`) que soporte caracteres especiales.
        with open(archivo_sql, 'r', encoding='utf-8') as file:
            # Leemos todo el contenido del archivo y lo guardamos en la variable sql.
            sql = file.read()
        
        # Buscar datos en el archivo SQL
        # Definimos una expresión regular para identificar bloques INSERT INTO. Estos bloques contienen:
        # primero el Nombre de la tabla lo capturamos con capturamos con (\w+)
        # segundo las Columnas de la tabla las capturamos con ([^)]+)
        # tercero los Valores dentro de los registros los capturamos con `(.+?)`).
        # El re.DOTALL asegura que se interpreten saltos de línea dentro de los valores
        patron = r"INSERT INTO\s+(\w+)\s*\(([^)]+)\)\s+VALUES\s+(.+?)(?=INSERT INTO|$)"
        
        # re.findall busca todos los bloques INSERT INTO que coincidan con el patrón definido.
        tablas = re.findall(patron, sql, re.DOTALL | re.IGNORECASE)

        # Condición para manejar tablas faltantes:
        # Si la lista tablas está vacía, es decir, no se encontraron bloques INSERT INTO en el archivo,
        # mostramos un mensaje informando que no se encontraron datos y terminamos.
        if not tablas:
            print("No se encontraron datos.")
            # Con return, salimos de la función y no ejecutamos más código.
            return

        
        # Procesar cada tabla encontrada
        # Recorremos las tablas que se encontraron en el archivo SQL.
        # nombre_tabla contiene el nombre de la tabla.
        # columnas_texto contiene los nombres de las columnas de la tabla.
        # valores_texto contiene todos los registros (datos) de la tabla.
        for nombre_tabla, columnas_texto, valores_texto in tablas:
        
            
            # Separar las columnas usando split(',').
            # strip() elimina espacios extra en los nombres de las columnas.
            columnas = [col.strip() for col in columnas_texto.split(',')]
            
            # Buscamos cada registro (fila) para identificar valores entre paréntesis.
            registros = re.findall(r"\(([^)]+)\)", valores_texto)
            # Para cada registro, creamos una lista de filas.
            # Cada fila se limpia eliminando espacios y quitando comillas con .strip("'").
            filas = [[valor.strip().strip("'") for valor in registro.split(',')] for registro in registros]

            # Crear un DataFrame de pandas
            # Usamos pandas.DataFrame para crear una tabla con los datos procesados.
            # Las columnas corresponden a los nombres obtenidos de columnas.
            df = pd.DataFrame(filas, columns=columnas)
            
            # Guardar el DataFrame en un archivo CSV:
            # Guardamos la tabla como archivo CSV usando el nombre de la tabla (`nombre_tabla`).
            # index=False evita que el archivo incluya una columna de índice innecesaria.
            # encoding='utf-8' asegura que los caracteres especiales se guarden correctamente.
            df.to_csv(f"{nombre_tabla}.csv", index=False, encoding='utf-8')
            # Confirmación de creación del archivo CSV
            # Mostramos un mensaje indicando que el archivo CSV se creó correctamente, incluyendo la cantidad de registros procesados.
            print(f"{nombre_tabla}.csv creado con {len(df)} registros.")
            
        print("¡Proceso completado!")
    # Si ocurre algún error durante el proceso por ejemplo, si el archivo no existe, mostramos el error en pantalla.
    except Exception as e:
        print(f"Error: {e}")




