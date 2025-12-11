import pandas as pd
import matplotlib.pyplot as plt
import json

def cargar_datos():
    try:
        with open("Entregas.json", "r", encoding="utf-8") as f:
            entregas = json.load(f)
    except Exception as e:
        print("❌ Error al cargar Entregas.json:", e)
        entregas = []

    try:
        with open("Agentes.json", "r", encoding="utf-8") as f:
            agentes = json.load(f)
    except Exception as e:
        print("❌ Error al cargar Agentes.json:", e)
        agentes = []

    return entregas, agentes
