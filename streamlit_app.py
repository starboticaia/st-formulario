import streamlit as st
from datetime import date

with st.form("Introduzca sus datos"):
  nombre = st.text_input("Nombre del alumno")  
  fecha_nac = st.date()
  alergias = st.multiselect("Frutos secos", "Lácteos", "Gluten", "Otros")
  # El botón Enviar es obligatorio
  enviado = st.form_submit_button("Enviar")
  
  if enviado:
    hoy = date.today()
    edad_dias = hoy - fecha_nac
    st.write("Nombre",nombre)
    st.write("Edad",edad_dias)
