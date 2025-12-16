import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos. Asume que el archivo 'vehicles_us.csv' está en el mismo directorio.
try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no fue encontrado. Asegúrate de que esté en el mismo directorio.")
    st.stop() # Detiene la ejecución si no se encuentran los datos.

# -----------------
# 1. Encabezado
# -----------------
st.header('Análisis de Vehículos Usados en EE. UU.')

# Mostrar las primeras filas del dataframe (opcional, para verificación)
st.subheader('Vista previa de los datos')
st.write(car_data.head())


# -----------------
# 2. Histograma
# -----------------

# Crear el botón del Histograma
hist_button = st.button('Construir Histograma de Kilometraje') 

if hist_button: # Si se hace clic en el botón del histograma
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches (distribución del odómetro)')
    
    # Crear un histograma de la columna 'odometer'
    fig = px.histogram(car_data, x="odometer", title='Distribución del Kilometraje (Odómetro)')

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# -----------------
# 3. Gráfico de Dispersión
# -----------------

# Crear el botón del Gráfico de Dispersión
scatter_button = st.button('Construir Gráfico de Dispersión de Precio vs. Kilometraje') 

if scatter_button: # Si se hace clic en el botón de dispersión
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión de precio vs. kilometraje.')
    
    # Crear un gráfico de dispersión de 'price' vs 'odometer', coloreado por 'condition'
    fig = px.scatter(car_data, x="odometer", y="price", color="condition",
                     title='Precio vs. Kilometraje por Condición del Vehículo')

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)