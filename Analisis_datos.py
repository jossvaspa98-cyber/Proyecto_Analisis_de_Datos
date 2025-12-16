
import csv
import pandas as pd
import matplotlib.pyplot as plt


def entregas_por_agente(df_entregas, df_agentes):
    try:
        print("\n🔍 Análisis: Entregas por Agente")

        # Normalización de nombres de columnas
        df_entregas.columns = df_entregas.columns.str.strip().str.lower()
        df_agentes.columns = df_agentes.columns.str.strip().str.lower()

        # Agrupar por ID de agente
        conteo = df_entregas['id_agente'].value_counts().reset_index()
        conteo.columns = ['id_agente', 'total_entregas']

        # Unir con la tabla de agentes
        df_resultado = pd.merge(conteo, df_agentes, on='id_agente', how='left')

        # Obtener top 5
        top_agentes = df_resultado.nlargest(5, 'total_entregas')

        # ✅ Imprimir columnas que sí existen
        print(top_agentes[['id_agente', 'nombre', 'correo', 'fecha_nacimiento', 'total_entregas']])

        # Gráfico
        plt.figure(figsize=(8, 5))
        plt.bar(top_agentes['nombre'], top_agentes['total_entregas'], color='skyblue')
        plt.title("Top 5 Agentes con más Entregas")
        plt.xlabel("Agente")
        plt.ylabel("Cantidad de Entregas")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("❌ Error en el análisis de entregas por agente:", e)

    
def entregas_por_hora(entregas):
    try:
        entregas.columns = entregas.columns.str.lower().str.strip()

        # Convertir hora de entrega a datetime
        entregas['hora_inicio'] = pd.to_datetime(entregas['hora_inicio'], errors='coerce')

        # Extraer hora como entero
        entregas['hora'] = entregas['hora_inicio'].dt.hour

        conteo = entregas['hora'].value_counts().sort_index()

        print("\n🕒 Cantidad de entregas por hora del día:")
        print(conteo)
        

        plt.figure(figsize=(10, 5))
        plt.title('Entregas por hora del día')
        plt.xlabel('Hora del día')
        plt.ylabel('Cantidad de entregas')
        plt.grid(True)
        plt.xticks(range(24))
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("❌ Error en el análisis por hora:", e)


# 📌 Función para analizar la distribución de peso de los paquetes
def distribucion_peso(df_entregas):
    try:
        print("\n🔍 Análisis: Distribución del Peso de los Paquetes")

        # Convertir a numérico (por si viene texto o hay errores)
        df_entregas['peso_kg'] = pd.to_numeric(df_entregas['peso_kg'], errors='coerce')

        # Eliminar nulos
        df_peso = df_entregas.dropna(subset=['peso_kg'])

        # 📊 Histograma
        plt.figure(figsize=(8, 5))
        plt.hist(df_peso['peso_kg'], bins=15, color='lightgreen', edgecolor='black')
        plt.title("Distribución de Pesos de Paquetes")
        plt.xlabel("Peso del Paquete (kg)")
        plt.ylabel("Cantidad de Entregas")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("❌ Error al analizar la distribución del peso:", e)

    
    
def total_entregado_por_tipo_vehiculo(entregas, vehiculos, tiposvehiculos):
    try:
        # Normalizar nombres de columnas
        entregas.columns = entregas.columns.str.lower().str.strip()
        vehiculos.columns = vehiculos.columns.str.lower().str.strip()
        tiposvehiculos.columns = tiposvehiculos.columns.str.lower().str.strip()

        # Unir las tablas
        df = pd.merge(entregas, vehiculos, on='id_vehiculo')
        df = pd.merge(df, tiposvehiculos, on='id_tipo')

        # Agrupar por tipo de vehículo y sumar peso
        resumen = df.groupby('descripcion')['peso_kg'].sum().reset_index().sort_values(by='peso_kg', ascending=False)

        print("\n📦 Total entregado por tipo de vehículo:")
        print(resumen)

        # Gráfico
        plt.figure(figsize=(8, 5))
        plt.title('Total entregado por tipo de vehículo')
        plt.ylabel('Peso entregado (kg)')
        plt.xlabel('Tipo de vehículo')
        plt.bar(resumen['descripcion'], resumen['peso_kg'], color='lightgreen')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("❌ Error en el análisis por tipo de vehículo:", e)

        
def top_clientes_con_mas_entregas(entregas, clientes):
        try:
            entregas.columns = entregas.columns.str.lower().str.strip()
            clientes.columns = clientes.columns.str.lower().str.strip()


            conteo = entregas['id_cliente'].value_counts().reset_index()
            conteo.columns = ['id_cliente', 'cantidad']


            df = pd.merge(conteo, clientes, on='id_cliente')
            top = df.sort_values(by='cantidad', ascending=False).head(5)


            print("\n🏆 Top 5 clientes con más entregas:")
            print(top[['id_cliente,nombre,direccion,correo']])


            plt.figure(figsize=(8, 5))
            plt.title('Top 5 clientes con más entregas')
            plt.xlabel('Cantidad de entregas')
            plt.ylabel('Cliente')
            plt.tight_layout()
            plt.show()


        except Exception as e:
            print("❌ Error en el análisis de clientes:", e)
            
def vehiculo_mas_eficiente(entregas, vehiculos):
    
        try:
            entregas.columns = entregas.columns.str.lower().str.strip()
            vehiculos.columns = vehiculos.columns.str.lower().str.strip()


            resumen = entregas.groupby('id_vehiculo').agg({
            'peso_kg': 'sum',
            'id_entrega': 'count'
            }).reset_index()


            resumen.columns = ['id_vehiculo', 'total_peso', 'num_entregas']
            resumen['eficiencia_kg_por_viaje'] = resumen['total_peso'] / resumen['num_entregas']


            resumen = pd.merge(resumen, vehiculos, on='id_vehiculo')
            resumen = resumen.sort_values(by='eficiencia_kg_por_viaje', ascending=False)


            print("\n🚚 Vehículos más eficientes (kg por viaje):")
            print(resumen[['placa', 'marca', 'modelo', 'eficiencia_kg_por_viaje']].head(5))


            plt.figure(figsize=(9, 5))
            plt.title('Top 5 vehículos más eficientes')
            plt.xlabel('Kg entregados por viaje')
            plt.ylabel('Placa')
            plt.tight_layout()
            plt.show()


        except Exception as e:
            print("❌ Error en el análisis de eficiencia:", e)
            
# Análisis 4: Ingresos totales por cliente (kg entregado x precio fijo)
def ingresos_totales_por_cliente(entregas, clientes):
        try:
            entregas.columns = entregas.columns.str.lower().str.strip()
            clientes.columns = clientes.columns.str.lower().str.strip()


            # Suponemos que el ingreso se calcula por total_pago o por peso_kg * tarifa
            resumen = entregas.groupby('id_cliente').agg({
            'total_pago': 'sum'
            }).reset_index()


            df = pd.merge(resumen, clientes, on='id_cliente')
            df = df.sort_values(by='total_pago', ascending=False).head(10)


            print("\n💰 Clientes con mayor pago acumulado:")
            print(df[['nom_cliente', 'apellido1', 'total_pago']])


            plt.figure(figsize=(9, 5))
            plt.title('Top 10 clientes por ingresos generados')
            plt.xlabel('Total pagado')
            plt.ylabel('Cliente')
            plt.tight_layout()
            plt.show()


        except Exception as e:
            print("❌ Error en el análisis de ingresos por cliente:", e)
            
            
# Análisis 5: Distribución de entregas por hora (para ver picos de demanda)
