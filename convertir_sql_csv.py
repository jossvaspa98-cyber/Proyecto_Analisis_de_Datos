import pandas as pd
import re

def convertir_sql_a_csv(archivo_sql):
    
    print("=" * 60)
    print("CONVIRTIENDO SQL A CSV")
    print("=" * 60)
    
    # PASO 1: Leer el archivo SQL
    print(f"\n📂 Leyendo archivo: {archivo_sql}")
    
    try:
        with open(archivo_sql, 'r', encoding='utf-8') as file:
            sql = file.read()
        print("✓ Archivo leído correctamente")
    except:
        # Si falla con utf-8, intentar con latin-1
        with open(archivo_sql, 'r', encoding='latin-1') as file:
            sql = file.read()
        print("✓ Archivo leído correctamente (latin-1)")
    
    # PASO 2: Encontrar todas las tablas
    print("\n🔍 Buscando tablas...")
    
    # Buscar: INSERT INTO nombre_tabla (columna1, columna2) VALUES
    patron = r"INSERT INTO\s+(\w+)\s*\(([^)]+)\)\s+VALUES\s+(.+?)(?=INSERT INTO|$)"
    tablas_encontradas = re.findall(patron, sql, re.DOTALL | re.IGNORECASE)
    
    if not tablas_encontradas:
        print("❌ No se encontraron tablas")
        return
    
    print(f"✓ Se encontraron {len(tablas_encontradas)} tablas\n")
    
    # PASO 3: Procesar cada tabla
    for nombre_tabla, columnas_texto, valores_texto in tablas_encontradas:
        
        print(f"📊 Procesando tabla: {nombre_tabla}")
        
        # Obtener nombres de columnas
        columnas = [col.strip() for col in columnas_texto.split(',')]
        
        # Encontrar todos los registros entre paréntesis
        registros = re.findall(r"\(([^)]+)\)", valores_texto)
        
        # Crear lista para guardar las filas
        filas = []
        
        # Procesar cada registro
        for registro in registros:
            # Dividir por comas y limpiar
            valores = []
            partes = registro.split(',')
            
            for parte in partes:
                # Quitar comillas y espacios
                valor = parte.strip()
                if valor.startswith("'") and valor.endswith("'"):
                    valor = valor[1:-1]  # Quitar comillas
                elif valor == 'NULL':
                    valor = ''  # NULL se vuelve vacío
                valores.append(valor)
            
            filas.append(valores)
        
        # PASO 4: Crear DataFrame y guardar CSV
        df = pd.DataFrame(filas, columns=columnas)
        
        nombre_archivo = f"{nombre_tabla}.csv"
        df.to_csv(nombre_archivo, index=False, encoding='utf-8')
        
        print(f"  ✓ {nombre_archivo} creado - {len(df)} registros")
    
    print("\n" + "=" * 60)
    print("✅ ¡Todos los archivos CSV fueron")




