import streamlit as st
from supabase import create_client

# 1. Tus credenciales de Supabase (Copia las tuyas de Project Settings -> API)
SUPABASE_URL = "https://jjruyavjxzhibfgmnatxu.supabase.co"
SUPABASE_KEY = "sb_publishable_euk3_MspnBq1DI7TMPFlPw_1mf8gXHm"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("Mi Primera App con Python y Supabase 🚀")

# 2. Formulario para registrar
with st.form("form_reg"):
    nombre = st.text_input("Escribe un nombre:")
    enviado = st.form_submit_button("Guardar en la nube")
    
    if enviado and nombre.strip():
        # Ojo aquí: usamos el nombre exacto de tu tabla "REQUERIMIENTO"
        supabase.table("REQUERIMIENTO").insert({"nombre": nombre}).execute()
        st.success(f"¡'{nombre}' guardado exitosamente!")

# 3. Mostrar los registros actuales
st.subheader("Registros en la Base de Datos")
respuesta = supabase.table("REQUERIMIENTO").select("*").execute()
datos = respuesta.data

if datos:
    st.dataframe(datos)
else:
    st.info("Aún no hay registros guardados.")