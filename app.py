import streamlit as st
import pandas as pd
import plotly.express as px
from analytics import calcular_ratios_financieros, evaluar_estres_macro

# Configuración del entorno web de Streamlit
st.set_page_config(page_title="MacroPulse Colombia", layout="wide", page_icon="📈")

st.title("📊 MacroPulse Colombia: Plataforma de Analítica y Riesgo Financiero")
st.markdown("---")

# Ejecutar el flujo analítico extrayendo desde la base de datos SQL
df_datos = calcular_ratios_financieros()

if df_datos is not None and not df_datos.empty:
    # Configuración de los controladores interactivos laterales
    st.sidebar.header("🎛️ Panel de Simulación Macro")
    
    lista_empresas = df_datos['empresa'].unique().tolist()
    empresa_seleccionada = st.sidebar.selectbox("Seleccione un Emisor BVC:", lista_empresas)
    
    tasa_simulada = st.sidebar.slider("Choque de Tasas de Interés (Puntos %):", 0.0, 5.0, 2.0, 0.5)
    
    # Recalcular el modelo predictivo con los inputs en tiempo real de la web
    df_simulado = evaluar_estres_macro(df_datos, incremento_tasa_bancaria=tasa_simulada)
    df_filtrado = df_simulado[df_simulado['empresa'] == empresa_seleccionada].iloc[-1]
    
    # Despliegue de métricas financieras de alto nivel
    st.subheader(f"Situación Crediticia y Estrés Financiero: {empresa_seleccionada}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Margen EBITDA Actual", value=f"{df_filtrado['margen_ebitda']:.1f}%")
    with col2:
        st.metric(label="Apalancamiento Neto", value=f"{df_filtrado['apalancamiento']:.2f}x")
    with col3:
        st.metric(label="Margen Estresado Simulado", value=f"{df_filtrado['nuevo_margen_ebitda']:.1f}%", delta=f"-{df_filtrado['caida_estimada_utilidad']:.1f}%")
    with col4:
        st.metric(label="Nivel de Riesgo Corporativo", value=df_filtrado['alerta_riesgo'])

    st.markdown("---")
    
    # Gráficos dinámicos con Plotly Express
    st.subheader("Tendencia de Márgenes Operativos Históricos")
    df_grafico = df_simulado[df_simulado['empresa'] == empresa_seleccionada]
    
    fig = px.line(df_grafico, x='periodo', y='margen_ebitda', text='margen_ebitda',
                  title=f"Evolución del Margen EBITDA por Periodo Fiscal para {empresa_seleccionada}",
                  labels={'periodo': 'Trimestre', 'margen_ebitda': 'Margen %'})
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='top center')
    
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Error crítico de inicialización de datos. Asegúrate de ejecutar el flujo de datos previo en la terminal corporativa.")
