import pandas as pd

def limpieza_datos():
    try:
        # -------------------------------
        # CLIENTES
        # -------------------------------
        df_clientes = pd.read_json("Clientes.json")
        df_clientes.columns = ["nombre", "direccion", "correo"]

        df_clientes["nombre"] = df_clientes["nombre"].str.strip().str.title()
        df_clientes["direccion"] = df_clientes["direccion"].str.strip().str.title()
        df_clientes["correo"] = df_clientes["correo"].str.strip().str.lower()

        df_clientes.to_json("Clientes_limpio.json", orient="records", force_ascii=False, indent=4)

        # -------------------------------
        # AGENTES
        # -------------------------------
        df_agentes = pd.read_json("Agentes.json")
        df_agentes.columns = ["nombre", "correo", "fecha_nacimiento"]

        df_agentes["nombre"] = df_agentes["nombre"].str.strip().str.title()
        df_agentes["correo"] = df_agentes["correo"].str.strip().str.lower()
        df_agentes["fecha_nacimiento"] = pd.to_datetime(df_agentes["fecha_nacimiento"], errors="coerce")

        df_agentes.to_json("Agentes_limpio.json", orient="records", force_ascii=False, indent=4)

        # -------------------------------
        # ENTREGAS
        # -------------------------------
        df_entregas = pd.read_json("Entregas.json")
        df_entregas.columns = [
            "id_agente", "id_cliente", "id_vehiculo", "fecha", "hora_inicio",
            "hora_fin", "estado", "distancia_km", "peso_kg", "total_pago"
        ]

        df_entregas["estado"] = df_entregas["estado"].str.strip().str.title()
        df_entregas["fecha"] = pd.to_datetime(df_entregas["fecha"], errors="coerce")
        df_entregas["hora_inicio"] = pd.to_datetime(df_entregas["hora_inicio"], format="%H:%M", errors="coerce").dt.time
        df_entregas["hora_fin"] = pd.to_datetime(df_entregas["hora_fin"], format="%H:%M", errors="coerce").dt.time

        df_entregas = df_entregas.drop_duplicates()

        df_entregas.to_json("Entregas_limpio.json", orient="records", force_ascii=False, indent=4)

        # -------------------------------
        # VEHICULOS
        # -------------------------------
        df_vehiculos = pd.read_json("Vehiculos.json")
        df_vehiculos.columns = ["id_agente", "tipo_id", "placa", "marca", "modelo"]

        df_vehiculos["placa"] = df_vehiculos["placa"].astype(str).str.strip().str.upper()
        df_vehiculos["marca"] = df_vehiculos["marca"].str.strip().str.title()
        df_vehiculos["modelo"] = df_vehiculos["modelo"].str.strip().str.title()

        df_vehiculos.to_json("Vehiculos_limpio.json", orient="records", force_ascii=False, indent=4)

        # -------------------------------
        # TIPOS VEHICULOS
        # -------------------------------
        df_tipos = pd.read_json("TiposVehiculos.json")
        df_tipos.columns = ["descripcion"]

        df_tipos["descripcion"] = df_tipos["descripcion"].str.strip().str.title()

        df_tipos.to_json("TiposVehiculos_limpio.json", orient="records", force_ascii=False, indent=4)

        print("✅ Todos los datos fueron limpiados y guardados correctamente.")

    except Exception as e:
        print("❌ Ocurrió un error durante la limpieza de datos:")
        print(f"   {e} ({type(e).__name__})")
