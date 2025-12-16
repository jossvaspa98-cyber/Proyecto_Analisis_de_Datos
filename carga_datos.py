import pandas as pd


def cargar_datos():

    try:
        agentes = pd.read_csv("Agentes.csv")
        clientes = pd.read_csv("Clientes.csv")
        entregas = pd.read_csv("Entregas.csv")
        vehiculos = pd.read_csv("Vehiculos.csv")
        tipos_vehiculos = pd.read_csv("TiposVehiculos.csv")


        # Normalización básica (visto en clase): quitar espacios, pasar columnas a minúsculas
        agentes.columns = agentes.columns.str.lower().str.strip()
        clientes.columns = clientes.columns.str.lower().str.strip()
        entregas.columns = entregas.columns.str.lower().str.strip()
        vehiculos.columns = vehiculos.columns.str.lower().str.strip()
        tipos_vehiculos.columns = tipos_vehiculos.columns.str.lower().str.strip()
            

        return agentes, clientes, entregas, vehiculos, tipos_vehiculos
    except Exception as e:
        print(f"❌ Error al cargar los archivos: {e}")
        return None, None, None, None, None