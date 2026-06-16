import os
import pandas as pd
from sqlalchemy import create_engine, text

# Definir la ruta de la base de datos local en la carpeta del proyecto
DB_NAME = "macropulse.db"
engine = create_engine(f"sqlite:///{DB_NAME}")

def inicializar_base_de_datos():
    """Crea las tablas necesarias si no existen en la base de datos."""
    print("Inicializando base de datos relacional...")
    
    with engine.connect() as conexion:
        # 1. Tabla para almacenar variables macroeconómicas
        conexion.execute(text("""
            CREATE TABLE IF NOT EXISTS tabla_macro (
                fecha DATE PRIMARY KEY,
                trm REAL,
                inflacion REAL
            );
        """))
        
        # 2. Tabla para almacenar estados financieros de empresas
        conexion.execute(text("""
            CREATE TABLE IF NOT EXISTS tabla_corporativa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nit TEXT,
                empresa TEXT,
                periodo TEXT,
                ingresos REAL,
                ebitda REAL,
                deuda_total REAL,
                patrimonio REAL,
                UNIQUE(nit, periodo) -- Evita duplicar estados financieros del mismo trimestre
            );
        """))
        conexion.commit() # Asegura guardar los cambios en la estructura
    print("¡Base de datos y tablas listas para operar!")

def guardar_datos_macro(df_macro):
    """Guarda o actualiza los datos macro en la base de datos."""
    if df_macro is None or df_macro.empty:
        return
    
    print("Guardando datos macroeconómicos en SQL...")
    try:
        # Usamos un bloque de conexión limpia para evitar bloqueos del archivo SQLite
        with engine.begin() as conn:
            df_macro.to_sql('tabla_macro', con=conn, if_exists='append', index=False, chunksize=500)
        print("Datos macro guardados exitosamente.")
    except Exception as e:
        print(f"Nota: Los datos macro ya se encuentran actualizados en la BD. ({e})")

if __name__ == "__main__":
    inicializar_base_de_datos()
