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

st.markdown("# Туризм")

# подзаголовок
st.subheader("муниципальное образование город Алексин")

# заголовок
st.header("визуализация результатов опроса по развитию туризма")

# ----- оформление боковой панели -----
st.sidebar.markdown("# главная page 🎈")

# Название боковой панели
st.sidebar.title("что-то")

# разделительная полоска
st.sidebar.divider()

# переключатель пола
gender = st.sidebar.radio("выберите пол респондентов: ", ('все','муж','жен'), horizontal=True)

# ещё разделительная полоска
st.sidebar.divider()

# переключатель возраста
age = st.sidebar.radio("укажите возраст респондентов: ", ('все','до 35', '36-45','46-55', 'старше 55'), horizontal=False)

# ещё разделительная полоска
st.sidebar.divider()

# переключатель отношения
att = st.sidebar.radio("укажите отношение респондентов к туристам: ", ('все','положительное', 'отрицательное'), horizontal=False)

# ещё разделительная полоска
st.sidebar.divider()

if gender == 'муж':
    st.sidebar.write("вы выбрали респондентов мужчин в возрасте", age)
else:
    st.sidebar.write("вы выбрали респондентов женщин в возрасте", age)
    
# ещё полоска
st.sidebar.divider()

def sidebar_input_features():
    gender = st.sidebar.multiselect("выберите пол респондентов: ", ["мужской","женский"], placeholder="пол респондентов")
    age = st.sidebar.multiselect("укажите возраст респондентов: ", ["до 35 лет", "36-45 лет","46-55 лет", "старше 55 лет"], placeholder="возраст респондентов")
    att = st.sidebar.multiselect("укажите отношение респондентов к туристам: ", ["положительное", "отрицательное"], placeholder="выбор отношение")

    translatetion = {
        "мужской": "муж",
        "женский": "жен",
        "до 35 лет": "до 35 лет",
        "36-45 лет": "36 - 45 лет",
        "46-55 лет": "46 - 55 лет",
        "старше 55 лет": "старше 55 лет",
        "положительное": "положительное",
        "отрицательное": "отрицательное"
    }

    data = {
        "пол": translatetion[gender],
        "возраст": translatetion[age],
        "отношение": translatetion[att],
    }

    df = pd.DataFrame(data)

    return df


# конец оформления боковой панели

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

options

df = pd.DataFrame(options)
df
dfnew = list(df[0])
dfnew

col1, col2 = st.columns(2)
col1.metric(label="пол", value='hjkkkkk')
col2.metric(label="возраст", value='ghbvk')


# ----- ПАРАМЕТРЫ РЕСПОНДЕНТОВ -----

st.success("Вы выбрали следующие параметры респондентов:")

col1, col2, col3 = st.columns(3)
col1.metric(label="пол", value=gender)
col2.metric(label="возраст", value=age)
col3.metric(label="отношение", value=att)

# полоска 
st.divider()

# читаем таблицу с опросом
df = pd.read_csv("datasets/Opros_po_razvitiiu_turizma.csv")

# данные из таблицы для графика
chart_data = pd.DataFrame(df, columns=["пол", "возраст", "отношение"])

# фильтр таблицы для графиков
# ..............................!!!!!!!!!!!!!!!!!!!!!!!!!!!
st.dataframe(chart_data)

options1 = ['муж', 'жен']
# options2 = ['до 35 лет', '', '', '', 'старше 55 лет']
options3 = ['положительное', 'отрицательное']
options3

genderist = st.multiselect("выберите пол респондентов: ", ["мужской","женский"], placeholder="пол респондентов")
gend = pd.DataFrame(genderist)


# rslt_df = df[(df.пол == 'муж') & (df.возраст == 'до 35 лет') & (df.отношение == 'положительное')]
rslt_df = df[(df.пол.isin(gend)) & (df.возраст == 'до 35 лет') & (df.отношение == 'положительное')]
st.dataframe(rslt_df)

col1, col2 = st.columns(2)
col1.metric(label="график 1", value=gender)
col2.metric(label="график 2", value=age)


# график измененный 1
val_count  = chart_data['возраст'].value_counts()
val_count
df1 = chart_data['возраст'].value_counts().rename_axis('unique_values').reset_index(name='counts')
st.bar_chart(data=df1, x='unique_values', y='counts')

# график измененный 2
val_count  = chart_data['отношение'].value_counts()
val_count
df1 = chart_data['отношение'].value_counts().rename_axis('unique_values').reset_index(name='counts')
st.bar_chart(data=df1, x='unique_values', y='counts')



# таблица с опросом вывести на экран целиком
# st.dataframe(df)

# таблица с опросом вывести на экран только мероприятия
# st.dataframe(df["Какие событийные мероприятия, по Вашему мнению, будут интересны жителям и гостям города?"])


# фильтр таблицы

# rslt_df = df[(df.пол == 'муж') & (df.возраст == 'до 35 лет') & (df.отношение == 'положительное')] 
rslt_df = df[(df.пол == 'муж') & (df.возраст == age) & (df.отношение == 'положительное')]
st.dataframe(rslt_df)
st.info("ответы респондентов на вопрос: Какие событийные мероприятия, по Вашему мнению, будут интересны жителям и гостям города?")
st.dataframe(rslt_df["ответ"])


# Текст
st.sidebar.text("Просто текст")


st.sidebar.info("Information")
st.sidebar.warning("Warning")
st.sidebar.error("Error")
# st.snow()
# st.balloons()



if st.sidebar.button('я кнопка -  Нажми на меня'):
  st.sidebar.write('надпись - результат нажатия на кнопку!')



option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.sidebar.write('You selected:', option)



