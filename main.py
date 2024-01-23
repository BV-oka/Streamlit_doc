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



# с помощью st.line_chart(). Мы сгенерируем случайную выборку с помощью Numpy, а затем нанесем ее на график.

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# график

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['муж', 'жен', 'дети'])

st.line_chart(chart_data)

# "Energy Costs By Month"

chart_data = pd.DataFrame(
     [10, 13, 11],
     columns=["Energy Costs"])
 
st.bar_chart(chart_data)

# графики в песочницу
dfopr=pd.DataFrame([[101, 'ivanov', 'муж', 'да'], [102, 'петров', 'муж', 'нет'], [103, 'сидорова', 'жен', 'да'], [104, 'коровин', 'муж', 'нет'], [105, 'кузнецов', 'муж', 'да'], [106, 'дубова', 'жен', 'нет'], [107, 'зайкина', 'жен', 'да']], columns=['id', 'fio', 'gender', 'otvet'])
dfopr
val_count  = dfopr['gender'].value_counts()
val_count
df1 = dfopr['gender'].value_counts().rename_axis('unique_values').reset_index(name='counts')
st.bar_chart(data=df1, x='unique_values', y='counts')


dfopr1=pd.DataFrame([['Earth', 1], ['Moon', 0.606], ['Mars', 0.107], ['Венера', 0.807]], columns=['name', 'mass'])
st.bar_chart(data=dfopr1, x='name', y='mass')

st.markdown("# Туризм")
st.sidebar.markdown("# главная page 🎈")


# Название
st.sidebar.title("что-то")

# Заголовок
st.header("муниципальное образование город Алексин")

# Подзаголовок
st.subheader("визуализация результатов опроса по развитию туризма")

# полоска
st.sidebar.divider()

# переключатель пола
gender = st.sidebar.radio("выберите пол респондентов: ", ('все','муж','жен'), horizontal=True)

# ещё полоска
st.sidebar.divider()

# переключатель возраста
age = st.sidebar.radio("укажите возраст респондентов: ", ('все','до 35', '36-45','46-55', 'старше 55'), horizontal=False)

# ещё полоска
st.sidebar.divider()

# переключатель отношения
att = st.sidebar.radio("укажите отношение респондентов к туристам: ", ('все','положительное', 'отрицательное'), horizontal=False)

# ещё полоска
st.sidebar.divider()

st.success("Вы выбрали следующие параметры респондентов:")

col1, col2, col3 = st.columns(3)
col1.metric(label="пол", value=gender)
col2.metric(label="возраст", value=age)
col3.metric(label="отношение", value=att)


if gender == 'муж':
    st.sidebar.write("вы выбрали респондентов мужчин в возрасте", age)
else:
    st.sidebar.write("вы выбрали респондентов женщин в возрасте", age)
    
# ещё полоска
st.sidebar.divider()





