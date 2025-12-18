
import csv
import pandas as pd
import matplotlib.pyplot as plt


def analizar_ventas_por_periodo(entregas, fecha_inicio=None, fecha_fin=None):
    try:
        # Convertimos la lista de entregas a un DataFrame para trabajar más fácilmente con pandas
        entregas_df = pd.DataFrame(entregas)

        # Convertimos la columna 'fecha' a tipo datetime para poder hacer filtros de fechas
        entregas_df['fecha'] = pd.to_datetime(entregas_df['fecha'], errors='coerce')

        # Filtramos por fecha de inicio si fue proporcionada
        if fecha_inicio:
            entregas_df = entregas_df[entregas_df['fecha'] >= pd.to_datetime(fecha_inicio)]

        # Filtramos por fecha de fin si fue proporcionada
        if fecha_fin:
            entregas_df = entregas_df[entregas_df['fecha'] <= pd.to_datetime(fecha_fin)]

        # Calculamos la suma total de pagos realizados en ese período
        ingresos_totales = entregas_df['total_pago'].sum()

        #  Calculamos el promedio de pago por cada entrega
        ingresos_promedio = entregas_df['total_pago'].mean()

        # Contamos cuántas entregas se hicieron en total
        total_entregas = entregas_df.shape[0]

        # Imprimimos en pantalla los resultados obtenidos
        print("\n-----------------Análisis de Ventas-----------------\n")
        print(f"Ingresos Totales: ${ingresos_totales:.2f}")
        print(f"Ingresos Promedio por Entrega: ${ingresos_promedio:.2f}")
        print(f"Total de Entregas: {total_entregas}")

        # Agrupamos las entregas por fecha y sumamos los pagos por cada día
        ventas_por_dia = entregas_df.groupby('fecha')['total_pago'].sum().reset_index()

        # Creamos una gráfica de línea para ver las ventas por día
        plt.plot(ventas_por_dia['fecha'], ventas_por_dia['total_pago'], marker='o', color='blue')
        plt.title('Ventas Totales por Día')
        plt.xlabel('Fecha')
        plt.ylabel('Ingresos Totales ($)')
        plt.grid(True)
        plt.show()

    except Exception as e:
        # Si ocurre un error en cualquier parte del código, mostramos el error en consola
        print(f"❌ Error en el análisis de ventas: {e}")

def vehiculo_mas_usado(entregas, vehiculos, tiposVehiculos):
    try:
        # Convertimos los datos de entregas, vehículos y tipos de vehículos a DataFrames para realizar el análisis
        entregas_df = pd.DataFrame(entregas)
        vehiculos_df = pd.DataFrame(vehiculos)
        tiposVehiculos_df = pd.DataFrame(tiposVehiculos)

        # Contamos el número total de entregas realizadas por cada vehículo ('id_vehiculo')
        # - Utilizamos value_counts para obtener el conteo de cada vehículo.
        conteo = entregas_df['id_vehiculo'].value_counts().reset_index()
        conteo.columns = ['id_vehiculo', 'total_entregas']

        # Ordenamos los vehículos por la cantidad de entregas realizadas, mostrando solo los 5 principales
        conteo = conteo.sort_values(by='total_entregas', ascending=False).head(5)

        # Combinamos los datos de entregas con los vehículos y tipos de vehículos
        # - Esto añade información relevante como marca, modelo y descripción del vehículo usado.
        top_vehiculos = pd.merge(conteo, vehiculos_df, on="id_vehiculo")
        top_vehiculos = pd.merge(top_vehiculos, tiposVehiculos_df, on="id_tipo")

        # Mostramos un reporte tabular en la consola con los resultados
        print("\n-----------------Vehículos más usados-----------------\n")
        print(top_vehiculos[['marca', 'modelo', 'descripcion', 'total_entregas']].to_markdown(index=False, tablefmt="grid"))

        # Generamos un gráfico que muestra los modelos de vehículos más utilizados
        # - Esto permite visualizar qué vehículos tienen la mayor actividad.
        plt.bar(top_vehiculos['modelo'], top_vehiculos['total_entregas'], color='orange')
        plt.title('Vehículos más usados')
        plt.xlabel('Vehículo')
        plt.ylabel('Total de entregas')
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        # Manejo de errores: Imprimimos un mensaje si ocurre algún problema durante el análisis.
        print(f"❌ Ocurrió un error: {e}")


def cliente_top_entregas(entregas, clientes):
    try:
        # Convertimos los datos de entregas y clientes a DataFrames para realizar el análisis
        entregas_df = pd.DataFrame(entregas)
        clientes_df = pd.DataFrame(clientes)

        # Contamos el número total de entregas realizadas por cada cliente ('id_cliente')
        conteo_clientes = entregas_df['id_cliente'].value_counts().reset_index()
        conteo_clientes.columns = ['id_cliente', 'total_entregas']

        # Ordenamos los clientes por la cantidad de entregas realizadas, mostrando solo los 5 principales
        conteo_clientes = conteo_clientes.sort_values(by='total_entregas', ascending=False).head(5)

        # Combinamos los datos de entregas con información de clientes
        # - Esto añade detalles como el nombre y dirección del cliente.
        top_clientes = pd.merge(conteo_clientes, clientes_df, on="id_cliente")

        # Mostramos un reporte tabular en la consola con los resultados
        print("\n-----------------Clientes con más entregas-----------------\n")
        print(top_clientes[['nombre', 'direccion', 'total_entregas']].to_markdown(index=False, tablefmt="grid"))

        # Generamos un gráfico que muestra los clientes con más entregas realizadas
        # - Esto permite visualizar qué clientes son los más activos.
        plt.bar(top_clientes['nombre'], top_clientes['total_entregas'], color='green')
        plt.title('Clientes con más entregas')
        plt.xlabel('Cliente')
        plt.ylabel('Total de entregas')
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        # Manejo de errores: Imprimimos un mensaje si ocurre algún problema durante el análisis.
        print(f"❌ Ocurrió un error: {e}")


import pandas as pd
import matplotlib.pyplot as plt

def analizar_eficiencia_por_agente(entregas, agentes):
    try:
        # Convertir listas de datos en tablas usando pandas
        entregas_df = pd.DataFrame(entregas)
        agentes_df = pd.DataFrame(agentes)

        # Convertir horas de inicio y fin a formato fecha
        entregas_df['hora_inicio'] = pd.to_datetime(entregas_df['hora_inicio'], errors='coerce')
        entregas_df['hora_fin'] = pd.to_datetime(entregas_df['hora_fin'], errors='coerce')

        # Calcular el tiempo total de cada entrega en minutos
        entregas_df['duracion_min'] = (entregas_df['hora_fin'] - entregas_df['hora_inicio']).dt.total_seconds() / 60

        # Calcular la eficiencia como minutos por kilómetro
        entregas_df['eficiencia_min_km'] = entregas_df['duracion_min'] / entregas_df['distancia_km']

        # Agrupar por agente para calcular promedio de eficiencia y total de kilómetros
        eficiencia_por_agente = entregas_df.groupby('id_agente').agg({
            # Promedio de eficiencia por agente
            'eficiencia_min_km': 'mean',
            # Suma de kilómetros recorridos por agente
            'distancia_km': 'sum'
        }).reset_index()

        # Unir con los nombres de los agentes
        eficiencia_por_agente = pd.merge(eficiencia_por_agente, agentes_df, on='id_agente')

        # Ordenar por eficiencia (menor min/km = más eficiente) y luego tomar el top 3
        eficiencia_top_3 = eficiencia_por_agente.sort_values('eficiencia_min_km').head(3)

        # Mostrar tabla del top 3
        print("\n-----------------Top 3 Agentes Más Eficientes-----------------\n")
        # Visualización mejorada en formato Markdown con estilo de tabla grid
        print(eficiencia_top_3[['nombre', 'eficiencia_min_km', 'distancia_km']].to_markdown(index=False, tablefmt="grid"))

    except Exception as e:
        print(f"Error: {e}")



def analizar_tipo_entregas(entregas):
    try:
        # Convertimos la lista de entregas a un DataFrame de pandas para poder analizarla
        entregas_df = pd.DataFrame(entregas)

        # Contamos cuántas entregas hay por cada estado (Ej: "entregada", "pendiente", etc.)
        # value_counts() hace el conteo por cada valor único en la columna 'estado'
        tipo_entregas = entregas_df['estado'].value_counts().reset_index()
        # Renombramos las columnas para que tengan nombres más claros
        tipo_entregas.columns = ['estado', 'cantidad']

        # Mostramos los resultados como una tabla en la consola
        print("\n-----------------Estado de las Entregas-----------------\n")
        print(tipo_entregas.to_markdown(index=False, tablefmt="grid"))

        # Creamos un gráfico circular (torta/pie chart) para visualizar la proporción de cada estado
        # autopct='%1.1f%%' muestra el porcentaje en el gráfico
        plt.pie(tipo_entregas['cantidad'], labels=tipo_entregas['estado'], autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
        plt.title('Distribución de Entregas por Estado')
        # Muestra el gráfico en pantalla
        plt.show()

    except Exception as e:
        print(f"❌ Error en el análisis de tipo de entregas: {e}")



def analizar_horas_pico(entregas):
    try:
        # Convertimos la lista de entregas en un DataFrame para poder trabajar con pandas
        entregas_df = pd.DataFrame(entregas)

        # Convertimos la columna 'hora_inicio' a formato de fecha y hora
        # Esto es necesario para poder extraer la hora después
        entregas_df['hora_inicio'] = pd.to_datetime(entregas_df['hora_inicio'], errors='coerce')

        # Extraemos solamente la hora (0 a 23) de la columna 'hora_inicio'
        entregas_df['hora'] = entregas_df['hora_inicio'].dt.hour

        # Contamos cuántas entregas se hicieron por cada hora del día
        # sort_index() asegura que las horas estén en orden
        horas_pico = entregas_df['hora'].value_counts().sort_index().reset_index()

        # Renombramos las columnas para que tengan nombres más claros
        horas_pico.columns = ['hora', 'total_entregas']

        # Formateamos la hora para que se vea como "08:00", "14:00", etc.
        horas_pico['hora_formateada'] = horas_pico['hora'].apply(lambda h: f"{h:02d}:00")

        # Mostramos los resultados como una tabla
        print("\n-----------------Horas Pico-----------------\n")
        print(horas_pico[['hora_formateada', 'total_entregas']].to_markdown(index=False, tablefmt="grid"))

        # Creamos un gráfico de barras para visualizar en qué horas hay más entregas
        plt.bar(horas_pico['hora_formateada'], horas_pico['total_entregas'], color='orange')
        plt.title('Horas Pico de Entregas')    
        plt.xlabel('Hora')                        
        plt.ylabel('Número de Entregas')          
        plt.xticks(rotation=45)                    
        plt.show()                                 

    except Exception as e:
        # Si ocurre un error, se muestra un mensaje explicando el problema
        print(f"❌ Error en el análisis de horas pico: {e}")

