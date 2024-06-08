import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(layout="wide")
st.title("Simulador Población Estudiantil Colegio Mayor")

# Cargar el dataset
df = pd.read_csv('static/datasets/poblacion_estudiantil_colegio_mayor.csv')

# Definir las opciones únicas para los filtros
aniosU = sorted(df['a_o'].unique())
periodosU = sorted(df['per_odo'].unique())
programasU = sorted(df['programa'].unique())
metodologiasU = sorted(df['metodologia'].unique())

# -----------------------------------------------------------------------------------
def filtro1():
    col1, col2, col3 = st.columns(3)
    with col1:
        anio = st.selectbox("Año", aniosU)
    with col2:
        programa = st.selectbox("Programa", programasU)
    with col3:
        periodosU.append("Todos")
        periodo = st.selectbox("Período", periodosU)

    if periodo == "Todos":
        resultado = df[(df['a_o'] == anio) & (df['programa'] == programa)]
        # Grafico de barras
        periodos = sorted(df['per_odo'].unique())
        fig = go.Figure(data=[
            go.Bar(name='Cantidad Matriculados', x=periodos, y=resultado['cantidad_matriculados']),
            go.Bar(name='Hombres', x=periodos, y=resultado['hombres']),
            go.Bar(name='Mujeres', x=periodos, y=resultado['mujeres'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado = resultado.reset_index(drop=True) 
        st.subheader("Detalle del Programa")
        st.table(resultado[["programa", "cantidad_matriculados", "hombres", "mujeres"]])       
    else:   
        resultado = df[(df['a_o'] == anio) & (df['per_odo'] == periodo) & (df['programa'] == programa)]
        # Grafico de barras
        programas = resultado['programa']
        fig = go.Figure(data=[
            go.Bar(name='Cantidad Matriculados', x=programas, y=resultado['cantidad_matriculados']),
            go.Bar(name='Hombres', x=programas, y=resultado['hombres']),
            go.Bar(name='Mujeres', x=programas, y=resultado['mujeres'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado = resultado.reset_index(drop=True) 
        st.subheader("Detalle del Programa")
        st.table(resultado[["programa", "cantidad_matriculados", "hombres", "mujeres"]])

# -----------------------------------------------------------------------------------
def filtro2():
    col1, col2 = st.columns(2)
    with col1:
        anio = st.selectbox("Año", aniosU)
    with col2:
        programa = st.selectbox("Programa", programasU)
    resultado = df[(df['a_o'] == anio) & (df['programa'] == programa)]
   
    resultado = resultado.reset_index(drop=True)
    # Grafico de torta
    labels = ['Cantidad Matriculados', 'Hombres', 'Mujeres']
    valores = [resultado['cantidad_matriculados'].mean(), resultado['hombres'].mean(), resultado['mujeres'].mean()]
    fig = go.Figure(data=[go.Pie(labels=labels, values=valores, textinfo='label+percent', insidetextorientation='radial')])
    st.plotly_chart(fig, use_container_width=True)
    # Tabla
    st.table(resultado[["programa", "cantidad_matriculados", "hombres", "mujeres"]])

# -----------------------------------------------------------------------------------
filtros = [
    "Detalle de matrículas por programa y período",
    "Matrículas por programa y año"
]

filtro = st.selectbox("Filtros", filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()

