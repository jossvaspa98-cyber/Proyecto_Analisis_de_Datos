import pandas as pd

def limpieza_datos():
    
    
    try: 
        
        # --------------------------------------------
        # LIMPIAR TABLA CLIENTES
        # --------------------------------------------
        # Leer el archivo clientes.json
        # pd.read_json() convierte el JSON en una tabla (DataFrame)
        df_clientes = pd.read_json("clientes.json")
        #Se nombran las columnas
        df_clientes.columns = [
            "nom_cliente", "apellido1", "apellido2",
            "correo_electronico", "ced_cliente",
            "direccion_cliente", "id_distrito"
        ]
        # range(len(df_clientes)) significa "hazlo para cada fila"
        # len() cuenta cuántas filas hay
        # range() crea una secuencia de números: 0, 1, 2, 3...
        for i in range(len(df_clientes)):
            # .loc[i, "columna"] = accede a la fila i en esa columna
            # .strip() = quita espacios al inicio y al final
            # .title() = pone la primera letra en mayúscula
            df_clientes.loc[i, "nom_cliente"] = df_clientes.loc[i, "nom_cliente"].strip().title()
            df_clientes.loc[i, "apellido1"] = df_clientes.loc[i, "apellido1"].strip().title()
            df_clientes.loc[i, "apellido2"] = df_clientes.loc[i, "apellido2"].strip().title()
            # .lower() = pone todo en minúsculas
            df_clientes.loc[i, "correo_electronico"] = df_clientes.loc[i, "correo_electronico"].strip().lower()
        
        # --------------------------------------------
        # LIMPIAR TABLA AGENTES
        # --------------------------------------------
        # Leer el archivo agentes.json
        # pd.read_json() convierte el JSON en una tabla (DataFrame)
        df_agentes = pd.read_json("agentes.json")
        # Se nombran las columnas
        df_agentes.columns = [
            "id_agente", "nom_agente", "apellido1",
            "apellido2", "ced_agente", "id_distrito", "fecha_nacimiento"
        ]
        # Limpiamos el nombre y apellido de cada agente
        # range(len(df_agentes)) significa "hazlo para cada fila"
        # len() cuenta cuántas filas hay
        # range() crea una secuencia de números: 0, 1, 2, 3...
        for i in range(len(df_agentes)):
            # .loc[i, "columna"] = accede a la fila i en esa columna
            # .strip() = quita espacios al inicio y al final
            # .title() = pone la primera letra en mayúscula
            df_agentes.loc[i, "nom_agente"] = df_agentes.loc[i, "nom_agente"].strip().title()
            df_agentes.loc[i, "apellido1"] = df_agentes.loc[i, "apellido1"].strip().title()
            df_agentes.loc[i, "apellido2"] = df_agentes.loc[i, "apellido2"].strip().title()
            
            # --------------------------------------------
            # LIMPIAR TABLA ENTREGAS
            # --------------------------------------------
            # Leer el archivo entregas.json
            # pd.read_json() convierte el JSON en una tabla (DataFrame)
            df_entregas = pd.read_json("entregas.json")
        # Poner nombres a las columnas
        df_entregas.columns = [
            "id_entrega", "num_entrega", "id_cliente", "id_agente", 
            "id_tipo_vehiculo", "fecha", "hora_entrada_entrega", 
            "estado_entrega", "hora_entregado", "id_negocio", 
            "id_distrito", "distancia_entrega", "peso_paquete", 
            "impuesto", "total_pago"
        ]

        # Limpiar texto (quita espacios y pone mayúsculas)
        df_entregas["estado_entrega"] = df_entregas["estado_entrega"].str.strip().str.title()


        # Convertir fechas y horas
        columnas_fechas_horas={
        "fecha": "%m/%d/%Y",              # 12/08/2025
        "hora_entrada_entrega": "time",  # 10:30:00
        "hora_entregado": "time"         # 11:00:00
        }

        # Convertir números (lista de columnas que son números)
        columnas_numeros = [
            "id_entrega", "num_entrega", "id_cliente", "id_agente", 
            "id_tipo_vehiculo", "id_negocio", "id_distrito", 
            "distancia_entrega", "peso_paquete", "impuesto", "total_pago"
        ]

        # Convertir todas de una vez
        df_entregas[columnas_numeros] = df_entregas[columnas_numeros].apply(pd.to_numeric, errors="coerce")

        # Quitar duplicados y vacíos
        df_entregas = df_entregas.drop_duplicates().dropna()
        # --------------------------------------------
        # LIMPIAR TABLA VEHÍCULOS
        # --------------------------------------------
        # Leer el archivo vehiculos.json
        # pd.read_json() convierte el JSON en una tabla (DataFrame)
        df_vehiculos = pd.read_json("vehiculos.json")
        df_vehiculos.columns = ["placa", "marca", "modelo", "id_tipo", "id_vehiculo"]
            # Las placas se escriben en MAYÚSCULAS
            # .astype(str) = lo convierte a texto
            # .str.upper() = convierte en mayúsculas
        for i in range(len(df_vehiculos)):
            df_vehiculos["placa"] = df_vehiculos["placa"].astype(str).str.strip().str.upper()
            df_vehiculos.loc[i, "marca"] = df_vehiculos.loc[i, "marca"].strip().title()
            df_vehiculos.loc[i, "modelo"] = df_vehiculos.loc[i, "modelo"].strip().title()
        
        
        # --------------------------------------------
        # LIMPIAR TABLA TIPOS_VEHÍCULOS
        # --------------------------------------------
        # Leer el archivo tipos_vehiculos.json
        # pd.read_json() convierte el JSON en una tabla (DataFrame)
        df_tipos_vehiculos = pd.read_json("tipos_vehiculos.json")
        df_tipos_vehiculos.columns = ["tipo_vehiculo"]
        for i in range(len(df_tipos_vehiculos)):
            # Limpiamos cada tipo
            df_tipos_vehiculos.loc[i, "tipo_vehiculo"] = df_tipos_vehiculos.loc[i, "tipo_vehiculo"].strip().title()
        
        # --------------------------------------------
        # LIMPIAR TABLA PROVINCIAS
        # --------------------------------------------
        # Leer el archivo provincias.json
        # pd.read_json() convierte el JSON en una tabla (DataFrame)
        df_provincias = pd.read_json("provincias.json")
        df_provincias.columns = ["nom_provincia"]
        for i in range(len(df_provincias)):
            # Limpiamos el nombre de cada provincia
            df_provincias.loc[i, "nom_provincia"] = df_provincias.loc[i, "nom_provincia"].strip().title()
        
        # --------------------------------------------
        # LIMPIAR TABLA CANTONES
        # --------------------------------------------
        # Leer el archivo cantones.json
        # pd.read_json() convierte el JSON en una tabla (DataFrame)
        df_cantones = pd.read_json("cantones.json")
        df_cantones.columns = ["nom_canton", "id_provincia"]
        for i in range(len(df_cantones)):
            # Limpiamos el nombre de cada cantón
            df_cantones.loc[i, "nom_canton"] = df_cantones.loc[i, "nom_canton"].strip().title()
        
        # --------------------------------------------
        # LIMPIAR TABLA DISTRITOS
        # --------------------------------------------
        # Leer el archivo distritos.json
        # pd.read_json() convierte el JSON en una tabla (DataFrame)
        df_distritos = pd.read_json("distritos.json")
        df_distritos.columns = ["nom_distrito", "id_canton"]
        for i in range(len(df_distritos)):
            # Limpiamos el nombre de cada distrito
            df_distritos.loc[i, "nom_distrito"] = df_distritos.loc[i, "nom_distrito"].strip().title()
        # Mostramos un mensaje de que todo salió bien!
        print(" Todos los datos han sido limpiados correctamente.")
        
        return (
        # Devolvemos todas las tablas limpias
        # return es como decir aquí está el resultado
            df_clientes, df_agentes, df_entregas, df_vehiculos,
            df_tipos_vehiculos, df_provincias, df_cantones, df_distritos
        )
    

    except Exception as error:
        # Imprime qué fue lo que salió mal
        # Retornamos None que significa "nada" o "vacío"
        # Esto ayuda a saber que algo falló
        print("❌ Ocurrió un error al cargar o limpiar los datos:")
        print(error)
        return None
    