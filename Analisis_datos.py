import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------
# ANÁLISIS 1: ENTREGAS POR AGENTE
#-------------------------------------------
def analisis_entregas_por_agente():

    try:
        
            df_agentes = pd.read_json("agentes.json")
            df_entregas = pd.read_json("entregas.json")
            df_clientes = pd.read_json("clientes.json")
            
            # Limpiar nombres de columnas
            for df in [df_entregas, df_agentes, df_clientes,]:
                df.columns = df.columns.str.strip().lower().titile()

            print("✓ Datos cargados correctamente")
            print(f"  - Entregas: {len(df_entregas)}")
            print(f"  - Agentes: {len(df_agentes)}")
            print(f"  - Clientes: {len(df_clientes)}")
            
                # Cargar datos limpios
                

            print("\n" + "=" * 60)
            print("📊 ANÁLISIS 1: Entregas por Agente")
            print("=" * 60)

            # Contar entregas por agente
            conteo_entregas = df_entregas['id_agente'].value_counts().reset_index()
            conteo_entregas.columns = ['id_agente', 'cantidad_entregas']

                # Unir con nombres de agentes
            df_agente_entregas = pd.merge(
                conteo_entregas, 
                df_agentes[['id_agente', 'nom_agente']], 
                on='id_agente', 
                how='left'
            )

                # Ordenar de mayor a menor
            df_agente_entregas = df_agente_entregas.sort_values(by='cantidad_entregas', ascending=False)

            print("\nTop 5 agentes con más entregas:")
            print(df_agente_entregas.head())

            # Gráfico
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.bar(df_agente_entregas['nom_agente'], 
                df_agente_entregas['cantidad_entregas'], 
                color='cornflowerblue', 
                edgecolor='black', 
                alpha=0.7)

            ax.set_title("Cantidad de Entregas por Agente", fontsize=16, fontweight='bold')
            ax.set_xlabel("Agente", fontsize=12)
            ax.set_ylabel("Cantidad de Entregas", fontsize=12)

            # Agregar valores encima de cada barra
            for i, v in enumerate(df_agente_entregas['cantidad_entregas']):
                    ax.text(i, v + 1, str(v), ha='center', va='bottom', fontweight='bold')
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()
                    plt.savefig("entregas_por_agente.png", dpi=300, bbox_inches='tight')
                    plt.show()

    except FileNotFoundError as e:
        print(f"Error: {e}. Asegúrate de que los archivos JSON existen.") 
    except Exception as e:
        print(f"Ocurrió un error durante el análisis: {e}") 
