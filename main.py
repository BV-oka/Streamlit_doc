# импортируем библиотеку streamlit
import streamlit as st
# импортируем библиотеку pandas
import pandas as pd
import numpy as np



# Название
st.title("Песочница")

# Заголовок
st.header("Это заголовок")

# Подзаголовок
st.subheader("Это подзаголовок")

# Текст
st.text("Просто текст")


# полоски
st.divider()
st.divider()

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
# st.snow()
# st.balloons()

if st.button('Нажми на меня'):
  st.write('Привет, мир!')


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


