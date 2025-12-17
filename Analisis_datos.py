
import csv
import pandas as pd
import matplotlib.pyplot as plt


def agentes_mas_eficientes_por_peso(entregas, agentes):
    try:
        print("\n🚚 Análisis: Agentes más eficientes por peso entregado")

        entregas.columns = entregas.columns.str.lower().str.strip()
        agentes.columns = agentes.columns.str.lower().str.strip()

        resumen = entregas.groupby('id_agente')['peso_kg'].sum().reset_index()
        resumen.columns = ['id_agente', 'peso_total_kg']

        resultado = pd.merge(resumen, agentes, on='id_agente', how='left')
        top = resultado.sort_values(by='peso_total_kg', ascending=False).head(5)

        print(top[['nombre', 'correo', 'peso_total_kg']])

    except Exception as e:
        print("❌ Error en el análisis de agentes eficientes:", e)


def vehiculo_mas_usado(entregas, vehiculos,tiposVehiculos):
    try:
        print("\n🚗 Análisis: Vehículo más utilizado")

        entregas.columns = entregas.columns.str.lower().str.strip()
        vehiculos.columns = vehiculos.columns.str.lower().str.strip()

        conteo = entregas['id_vehiculo'].value_counts().reset_index()
        conteo.columns = ['id_vehiculo', 'total_entregas']
        
        df = pd.merge(conteo, vehiculos, on='id_vehiculo', how='left')

        # Unir vehículos con su tipo/descripción
        df = pd.merge(df, tiposVehiculos, on='id_tipo', how='left')
        
        top = df.sort_values(by='total_entregas', ascending=False).head(3)

        print(top[['id_vehiculo', 'marca', 'modelo','descripcion','total_entregas']])

    except Exception as e:
        print("❌ Error en el análisis de vehículo más usado:", e)


def cliente_top_entregas(entregas, clientes):
    try:
        print("\n🏆 Análisis: Cliente con más entregas")
        entregas.columns = entregas.columns.str.lower().str.strip()
        clientes.columns = clientes.columns.str.lower().str.strip()
        conteo = entregas['id_cliente'].value_counts().reset_index()
        conteo.columns = ['id_cliente', 'total_entregas']
        resultado = pd.merge(conteo, clientes, on='id_cliente', how='left')
        top = resultado.sort_values(by='total_entregas', ascending=False).head(5)
        print(top[['id_cliente', 'nombre', 'direccion', 'total_entregas']])
    except Exception as e:
        print("❌ Error en el análisis de clientes con más entregas:", e)


def peso_promedio_por_tipo_vehiculo(entregas, vehiculos, tiposvehiculos):
    try:
        print("\n📦 Análisis: Peso promedio entregado por tipo de vehículo")
        # Normalización de columnas
        entregas.columns = entregas.columns.str.lower().str.strip()
        vehiculos.columns = vehiculos.columns.str.lower().str.strip()
        tiposvehiculos.columns = tiposvehiculos.columns.str.lower().str.strip()
        # Unir entregas con vehículos
        df = pd.merge(entregas, vehiculos, on='id_vehiculo', how='left')
        # Unir con tipos de vehículos
        df = pd.merge(df, tiposvehiculos, on='id_tipo', how='left')
        # Agrupar por descripción del vehículo
        promedio = (df.groupby('descripcion')['peso_kg'].mean().reset_index().sort_values(by='peso_kg', ascending=False))
        promedio.columns = ['tipo_vehiculo', 'peso_promedio_kg']
        print("\n📊 Peso promedio entregado por tipo de vehículo:")
        print(promedio)
        print(
            "\n💡 Interpretación estratégica:"
            "\nLos tipos de vehículo con mayor peso promedio son más adecuados"
            "\npara entregas pesadas y deben priorizarse para ese tipo de servicio."
        )
    except Exception as e:
        print("❌ Error en el análisis de peso promedio por tipo de vehículo:", e)





def hora_mas_activa(entregas):
    try:
        print("\n🕓 Análisis: Hora más activa del día")
        entregas.columns = entregas.columns.str.lower().str.strip()
        # Asegurar que la columna existe
        if 'hora_inicio' not in entregas.columns:
            print("⚠️ No existe la columna 'hora_inicio' en los datos.")
            return
        # Convertir a datetime y extraer hora
        entregas['hora_inicio'] = pd.to_datetime(entregas['hora_inicio'], errors='coerce')
        entregas['hora'] = entregas['hora_inicio'].dt.hour
        # Eliminar filas con hora nula
        entregas = entregas.dropna(subset=['hora'])
        conteo = entregas['hora'].value_counts().sort_index()
        # Validar que hay datos
                # Mostrar tabla con formato legible
        print("Entregas por hora:")
        for h, count in conteo.items():
            hora_legible = f"{h:02d}:00"
            print(f"{hora_legible} - {count} entregas")

        # Obtener la hora con más entregas
        hora_pico = conteo.idxmax()
        total = conteo.max()
        hora_formateada = f"{hora_pico:02d}:00"

        print(f"\n🔝 La hora con más entregas es: {hora_formateada} con {total} entregas")

    except Exception as e:
        print("❌ Error en el análisis de hora más activa:", e)