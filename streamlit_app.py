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
    # la diferencia está en días
    edad = (hoy - fecha_nac)/365
    st.write("Nombre",nombre)
    st.write("Edad",edad_dias)
