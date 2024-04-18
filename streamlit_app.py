import streamlit as st
import datetime

with st.form("Introduzca sus datos"):
  nombre = st.text_input("Nombre del alumno")  
  fecha_nac = st.date_input("Fecha de nacimiento")
  alergias = st.multiselect("Alergias",["Frutos secos", "Lácteos", "Gluten", "Otros"])
  # El botón Enviar es obligatorio
  enviado = st.form_submit_button("Enviar")
  
  if enviado:
    hoy = datetime.date.today()
    edad_dias = hoy - fecha_nac
    st.write("Nombre",nombre)
    st.write("Edad",edad_dias)
