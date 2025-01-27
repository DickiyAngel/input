import streamlit as st
name = st.text_input(f"Your name", key="name") #Поле для ввода текста
st.session_state.name #Вывод того, что бы введено в текстовое поле
st.session_state.name

result_file = open('name.txt', "w+")
result_file.write(name)
result_file.close()