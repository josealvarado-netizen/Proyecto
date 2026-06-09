import streamlit as st

# Agregamos un título
st.title("Mi primera Applet en Streamlit")

# Widget de entrada de datos
user_name = st.text_input("Ingresa tu nombre:")

# Slider dinámico
age = st.slider("Ingresa tu edad", min_value=5, max_value=99, value=10)

if st.button("Enviar"):
    st.write(f"Hola {user_name}, tu edad es {age}.")
    st.balloons()