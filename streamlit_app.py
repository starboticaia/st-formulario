import streamlit as st

with st.form("Introduzca sus datos"):
  nombre = st.text_input("Nombre")
  fecha_nac = st.date_input("Fecha de nacimiento")
  alergias = st.multiselect("Alergias",["Frutos secos", "Lácteos", "Gluten", "Otros"])
  # El botón Enviar es obligatorio
  enviado = st.form_submit_button("Enviar")
  
  if enviado:    
    st.write("Nombre",nombre)
    if alergias.length>0:
      st.write("Asegúrese de que ha especificado todas sus alergias.")            
    else:
      no_alergico = st.checkbox("Marque la casilla para confirmar que declara que no es alérgico")
      alergias = "Ninguna"

    resumen = f"""
    Nombre: {nombre}
    Edad: {edad}
    Alergias: {alergias}
    """
    
    st.download_button('Descargar resumen',resumen)   
