
# Proyecto de Análisis de Datos – VPDelivery

## Autor
María Josseth Vásquez Pacheco  
Curso: Programación  
Profesor: Andrés Mena A.

## Descripción
Este proyecto desarrolla un programa en Python para analizar los datos operativos de la empresa VPDelivery. 
El sistema permite evaluar entregas, agentes, vehículos y clientes, generando métricas y visualizaciones que apoyan la toma de decisiones.

El proyecto fue desarrollado siguiendo la metodología IteraFlex.

## Funcionalidades
El programa permite:
- Convertir una base de datos SQL en archivos CSV.
- Cargar datos desde archivos CSV.
- Analizar ventas por período.
- Identificar los vehículos más utilizados.
- Identificar los clientes con mayor cantidad de entregas.
- Analizar la eficiencia de los agentes.
- Analizar el estado de las entregas.
- Identificar las horas pico de entregas.


## Menú del sistema
Al ejecutar el programa se muestra el siguiente menú:

1. Carga de datos  
2. Ver ventas por periodo  
3. Ver vehículos más usados  
4. Ver clientes top de entregas  
5. Ver eficiencia por agente  
6. Ver tipos de entregas por estado  
7. Ver horas pico de entregas  
0. Salir  

## Conversión de SQL a CSV
El proyecto incluye un módulo que convierte un archivo SQL en archivos CSV para facilitar el análisis de datos.

La función convertir_sql_a_csv():
- Lee un archivo SQL que contiene sentencias INSERT INTO.
- Identifica automáticamente los nombres de las tablas y sus columnas.
- Extrae los registros de cada tabla utilizando expresiones regulares.
- Convierte los datos extraídos en DataFrames de pandas.
- Genera un archivo CSV por cada tabla encontrada.
- Muestra mensajes de confirmación indicando los archivos creados y la cantidad de registros.


## Carga de datos
El proyecto incluye un módulo encargado de cargar los datos desde archivos CSV.

La función cargar_datos():
- Lee los archivos Agentes.csv, Clientes.csv, Entregas.csv Vehiculos.csv y TiposVehiculos.csv.
- Carga cada archivo en un DataFrame de pandas.
- Normaliza los nombres de las columnas convirtiéndolos a minúsculas y eliminando espacios innecesarios.
- Devuelve los DataFrames listos para ser utilizados en los análisis.
- Maneja errores en caso de que algún archivo no exista o no pueda cargarse.

## Módulo de análisis de datos
El proyecto incluye un módulo encargado de realizar el análisis de los datos y generar visualizaciones.

Este módulo contiene las siguientes funciones:

### Análisis de ventas por período
La función analizar_ventas_por_periodo():
- Analiza los ingresos totales y el ingreso promedio por entrega.
- Permite filtrar los datos por fecha de inicio y fecha final.
- Cuenta el total de entregas realizadas.
- Genera un gráfico de líneas que muestra las ventas totales por día.

### Vehículos más usados
La función vehiculo_mas_usado():
- Identifica los vehículos con mayor cantidad de entregas.
- Combina información de entregas, vehículos y tipos de vehículos.
- Muestra un reporte tabular con marca, modelo y total de entregas.
- Genera un gráfico de barras para visualizar los vehículos más utilizados.

### Clientes con más entregas
La función cliente_top_entregas():
- Identifica los clientes con mayor número de entregas.
- Muestra los cinco clientes más acti

### Eficiencia por agente
La función analizar_eficiencia_por_agente():
- Calcula la duración de cada entrega en minutos.
- Calcula la eficiencia de los agentes en minutos por kilómetro.
- Identifica el top 3 de agentes más eficientes.
- Muestra los resultados en formato tabular.

### Estado de las entregas
La función analizar_tipo_entregas():
- Analiza la cantidad de entregas según su estado.
- Muestra una tabla con los estados de las entregas.
- Genera un gráfico circular que representa la distribución de los estados.

### Horas pico de entregas
La función analizar_horas_pico():
- Analiza las horas del día con mayor actividad de entregas.
- Muestra una tabla con el total de entregas por hora.
- Genera un gráfico de barras para visualizar las horas pico.