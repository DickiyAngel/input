import streamlit as st

name = st.text_input(f"Лучшая компания семечек?", key="name") #Поле для ввода текста
st.session_state.name #Вывод того, что бы введено в текстовое поле

dostup = 'Правильно'
zapret = 'Поешь говна, чушпан. Выбери другую компанию'

if name == 'Мартин' or name == 'мартин':
    st.text(dostup)
else:
    st.text(zapret)


result_file = open('семки.txt', "w+")
result_file.write(name)
result_file.close()