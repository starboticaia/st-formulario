import streamlit as st

enviado = False

with st.form("Introduzca sus datos"):
  nombre = st.text_input("Nombre")
  fecha_nac = st.date_input("Fecha de nacimiento")
  alergias = st.multiselect("Alergias",["Frutos secos", "Lácteos", "Gluten", "Otros"])
  # El botón Enviar es obligatorio
  enviado = st.form_submit_button("Enviar")

# no se puede poner otro botón dentro de un formulario
if enviado:    
  st.write("Nombre",nombre)
  if len(alergias)>0:
    st.write("Asegúrese de que ha especificado todas sus alergias.")            
  else:
    no_alergico = st.checkbox("Marque la casilla para confirmar que declara que no es alérgico")
    alergias = "Ninguna"

  resumen = f"""
  Nombre: {nombre}
  Fecha de nacimiento: {fecha_nac}
  Alergias: {alergias}
  """
  st.write(resumen)
  st.download_button("Descargar",resumen)
