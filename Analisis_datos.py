
import json
import pandas as pd
import matplotlib.pyplot as plt

def entregas_por_agente(entregas, agentes):
    try:
        for id_agente, agente in enumerate(agentes, start=1):
            agente["id_agente"] = id_agente
            
        for entrega in entregas:
            entrega["id_agente"] = int(entrega["id_agente"])

        conteo = {}
        for entrega in entregas:
            id_agente = entrega["id_agente"]
            conteo[id_agente] = conteo.get(id_agente, 0) + 1

        print("\n📦 Entregas por agente:")
        for agente in agentes:
            id_a = int(agente["id_agente"])
            nombre = agente["nombre"].strip().title()
            print(f"👤 {nombre}: {conteo.get(id_a, 0)} entregas")
        return conteo
    except Exception as e:
        print("❌ Error en entregas_por_agente:", e)
        return {}


def peso_promedio_por_agente(entregas, agentes):
    try:
        # Normalización: asegurar que peso esté como número
        for entrega in entregas:
            entrega["peso_kg"] = float(entrega["peso_kg"])
            entrega["id_agente"] = int(entrega["id_agente"])

        total_pesos = {}
        conteo = {}

        for entrega in entregas:
            id_agente = entrega["id_agente"]
            peso = entrega["peso_kg"]
            total_pesos[id_agente] = total_pesos.get(id_agente, 0) + peso
            conteo[id_agente] = conteo.get(id_agente, 0) + 1

        print("\n⚖️ Peso promedio por agente:")
        for agente in agentes:
            id_a = int(agente["id_agente"])
            nombre = agente["nombre"].strip().title()
            if conteo.get(id_a, 0) > 0:
                promedio = total_pesos[id_a] / conteo[id_a]
                print(f"👤 {nombre}: {promedio:.2f} kg")
    except Exception as e:
        print("❌ Error en peso_promedio_por_agente:", e)
        
        
def total_pago_por_agente(entregas, agentes):
    try:
        # Normalización: convertir total a float
        for entrega in entregas:
            entrega["id_agente"] = int(entrega["id_agente"])
            entrega["total_pago"] = float(entrega["total_pago"])

        totales = {}
        for entrega in entregas:
            id_agente = entrega["id_agente"]
            pago = entrega["total_pago"]
            totales[id_agente] = totales.get(id_agente, 0) + pago

        print("\n💰 Total cobrado por agente:")
        for agente in agentes:
            id_a = int(agente["id_agente"])
            nombre = agente["nombre"].strip().title()
            print(f"👤 {nombre}: ₡{totales.get(id_a, 0):,.2f}")
    except Exception as e:
        print("❌ Error en total_pago_por_agente:", e)
        
        
def entregas_por_dia(entregas):
    try:
        # Normalización: asegurar que la fecha tenga formato datetime
        df = pd.DataFrame(entregas)
        df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
        df["dia_semana"] = df["fecha"].dt.day_name()

        conteo = df["dia_semana"].value_counts().sort_index()

        print("\n📅 Entregas por día de la semana:")
        for dia, cantidad in conteo.items():
            print(f"📆 {dia}: {cantidad} entregas")
        return conteo
    except Exception as e:
        print("❌ Error en entregas_por_dia:", e)
        return {}
    
