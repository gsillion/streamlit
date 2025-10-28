import streamlit as st

st.title("Meu primeiro app Streamlit 🚀")
st.write("Olá! Este app está rodando no Streamlit Cloud.")
st.write("Digite algo abaixo:")

nome = st.text_input("Seu nome")
if nome:
    st.success(f"Bem-vindo(a), {nome}!")