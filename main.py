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


st.divider()

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# таблички

# интерактивная табличка
st.text("интерактивная табличка")

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# интерактивная с выделенным элементом
st.text("интерактивная табличка с выделенным элементом")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# статическая табличка

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


# переключатели
status = st.radio("выберите вариант: ", ('да', 'нет'))

if (status == 'да'):
    st.success("да")
else:
    st.success("нет")
    
  

status = st.radio("выберите вариант: ", ('да', 'нет'), horizontal=True)

if (status == 'да'):
    st.success("да")
else:
    st.success("нет")
    st.snow()



genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.success('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


# слайдеры

# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')



values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)







