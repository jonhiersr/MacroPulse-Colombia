import pandas as pd
import requests
from db_manager import inicializar_base_de_datos, guardar_datos_macro

def obtener_trm_historica(limite_datos=1000):
    """
    Se conecta a la API de datos abiertos de Colombia para extraer la TRM histórica.
    """
    print("Conectándose a la API de Datos Abiertos de Colombia...")
    url_api = f"https://datos.gov.co{limite_datos}"
    
    try:
        respuesta = requests.get(url_api)
        respuesta.raise_for_status()
        
        datos_crudos = respuesta.json()
        df = pd.DataFrame(datos_crudos)
        
        # -------------------------------------------------------------
        # PROCESAMIENTO Y LIMPIEZA DE DATOS
        # -------------------------------------------------------------
        df = df.rename(columns={'vigenciadesde': 'fecha', 'valor': 'trm'})
        
        # Formatear tipos de datos correctamente para análisis cuantitativo
        df['fecha'] = pd.to_datetime(df['fecha']).dt.strftime('%Y-%m-%d')
        df['trm'] = pd.to_numeric(df['trm'], errors='coerce')
        
        df = df.sort_values(by='fecha').reset_index(drop=True)
        print("¡Limpieza de datos macro completada con éxito!")
        return df[['fecha', 'trm']]
        
    except requests.exceptions.RequestException as e:
        print(f"Error crítico al conectarse a la API: {e}")
        return None

if __name__ == "__main__":
    # Inicializa la estructura SQL local primero
    inicializar_base_de_datos()
    
    # Descarga los últimos 100 registros históricos reales de la TRM
    df_trm = obtener_trm_historica(limite_datos=100)
    
    # Almacena los resultados en tu base de datos
    if df_trm is not None:
        guardar_datos_macro(df_trm)
