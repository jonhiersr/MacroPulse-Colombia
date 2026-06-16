import pandas as pd
from db_manager import engine

def simular_extraccion_superfinanciera():
    """
    Estructura y normaliza estados financieros corporativos de emisores de la BVC.
    """
    print("Iniciando extracción y normalización de reportes financieros bajo estándar NIIF...")
    
    # Valores expresados en miles de millones de COP
    data = {
        'nit': ['890903938', '890903938', '811031201', '811031201'],
        'empresa': ['Bancolombia', 'Bancolombia', 'Ecopetrol', 'Ecopetrol'],
        'periodo': ['2025-Q3', '2025-Q4', '2025-Q3', '2025-Q4'],
        'ingresos': [14200.0, 15100.0, 32400.0, 31100.0],
        'ebitda': [4100.0, 4300.0, 11200.0, 9800.0],
        'deuda_total': [12300.0, 11900.0, 48200.0, 49500.0],
        'patrimonio': [32000.0, 33500.0, 64000.0, 62100.0]
    }
    
    df_corporativo = pd.DataFrame(data)
    
    # Cast estricto de tipos cuantitativos
    df_corporativo['ingresos'] = df_corporativo['ingresos'].astype(float)
    df_corporativo['ebitda'] = df_corporativo['ebitda'].astype(float)
    df_corporativo['deuda_total'] = df_corporativo['deuda_total'].astype(float)
    df_corporativo['patrimonio'] = df_corporativo['patrimonio'].astype(float)
    
    return df_corporativo

def guardar_datos_corporativos(df_corp):
    """Inserta los estados financieros procesados en la base de datos SQL."""
    print("Insertando registros financieros corporativos en la base de datos...")
    try:
        with engine.begin() as conn:
            df_corp.to_sql('tabla_corporativa', con=conn, if_exists='append', index=False)
        print("¡Estados financieros consolidados en la base de datos con éxito!")
    except Exception as e:
        print(f"Aviso de restricción: Los registros financieros ya existen en SQL o hubo un fallo: {e}")

if __name__ == "__main__":
    df_financiero = simular_extraccion_superfinanciera()
    guardar_datos_corporativos(df_financiero)
