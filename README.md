🚗 Panel de Análisis de Vehículos Usados
🌟 Descripción Rápida
Esta es una aplicación web interactiva, creada con la librería Streamlit, diseñada para explorar y visualizar un conjunto de datos de anuncios de venta de vehículos usados (vehicles_us.csv).
Su objetivo es permitir a los usuarios generar gráficos clave para el Análisis Exploratorio de Datos (EDA) con solo pulsar un botón.
📊 Funcionalidades
La aplicación proporciona dos gráficos interactivos generados bajo demanda:
Histograma de Kilometraje (Odometer): Muestra la distribución de la frecuencia del kilometraje en el conjunto de datos.
Gráfico de Dispersión (Precio vs. Kilometraje): Muestra la relación entre el precio de venta y el kilometraje, permitiendo evaluar la correlación y el impacto de la condición del vehículo.
⚙️ Cómo Ejecutar Localmente
Para iniciar la aplicación en tu navegador:
Archivos Requeridos: Asegúrate de tener app.py, requirements.txt y vehicles_us.csv en la misma carpeta.
Instalar Dependencias: Instala las librerías necesarias (pandas, streamlit, plotly-express):
pip install -r requirements.txt



Iniciar la Aplicación: Abre tu terminal en la carpeta del proyecto y ejecuta:
streamlit run app.py



La aplicación se cargará automáticamente en tu navegador web.
