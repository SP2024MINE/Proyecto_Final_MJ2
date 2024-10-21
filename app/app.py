import streamlit as st
import pandas as pd
import requests

# Definir la URL de la API (esto debe reemplazarse con la URL real de la API)
api_url = "http://127.0.0.1:8000/predict"

st.title("Formulario de Datos para el Modelo")

# Campos numéricos
age = st.number_input("Edad:", min_value=0, max_value=120)
balance = st.number_input("Saldo promedio anual:", min_value=0)
day_of_week = st.number_input("Día del último contacto:", min_value=1, max_value=31)
campaign = st.number_input("Número de contactos realizados durante esta campaña:", min_value=1, max_value=60)

## Preguntar si hubo contacto en campañas previas si no 
camp_prev = st.selectbox('¿Contacto en campaña previa?:', ['yes', 'no'])

if camp_prev == 'yes':
    pdays = st.number_input("Número de días que pasaron después de que el cliente fue contactado por última vez desde una campaña anterior:", min_value=1, max_value=60)
    previous = st.number_input("Número de contactos realizados antes de esta campaña:", min_value=1, max_value=60)
else:
    pdays= -1
    previous = 0 

# Campos categóricos con selectores
job = st.selectbox("Ocupación:", ['management',  'technician',  'entrepreneur',  'retired',  'admin.',  'services',
                                         'blue-collar',  'self-employed', 'unemployed',  'housemaid',  'student'])
marital = st.selectbox("Estado civil:", ['married', 'single', 'divorced'])
education = st.selectbox("Nivel educativo:", ["Married-civ-spouse", "Divorced", "Never-married", 
                                                "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"])
default = st.selectbox('¿Tiene crédito en mora?:', ['yes', 'no'])
housing = st.selectbox('¿Tiene préstamo de vivienda?:', ['yes', 'no'])
loan = st.selectbox('¿Tiene préstamo personal?:' ['yes', 'no'])
month = st.selectbox('Mes del último contacto', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
                                                 'nov', 'dec'])

# Mostrar los datos capturados
if st.button("Mostrar datos"):
    st.write("Datos capturados:")
    st.write(f"Edad: {age}")
    st.write(f"Estado civil: {marital}")
    st.write(f"Nivel educativo: {education}")
    st.write(f"Ocupación: {job}")
    st.write(f"Crédito en mora: {default}")
    st.write(f"Préstamo de vivienda: {housing}")
    st.write(f"Préstamo personal: {loan}")
    st.write(f"Saldo promedio mensual: {balance}")
    st.write(f"Mes de último contacto: {month}")
    st.write(f"Día de último contacto: {day_of_week}")
    st.write(f"Número de contactos realizados: {campaign}")
    st.write(f"Contacto en campaña previa: {camp_prev}")
    if camp_prev == 'yes':
        st.write(f"Número de días que pasaron desde que el cliente fue contactado por última vez en una campaña anterior: {pdays}")
        st.write(f"Número de contactos realizados antes de esta campaña: {previous}")


