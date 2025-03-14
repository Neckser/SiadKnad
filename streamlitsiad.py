import streamlit as st
import requests

st.title("Погодное приложение")
file= st.file_uploader("Выберите файл", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.write("Содержимое вашего файла:")
    st.dataframe(df)
with st.form(key='my_form'):
    akey = st.text_input("Введите ваш API-key:") 
city = st.selectbox("Выберите город:", ['London', 'New York', 'Tokyo', 'Moscow', 'Madrid'])
if akey:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={akey}&units=metric"
    if st.button("Получить погоду"):
        request = requests.get(url)
        datatext = request.json()
        if datatext:
            temperature = datatext['main']['temp']
            desc = datatext['weather'][0]['description']            
            st.success(f"Температура в {city}: {temperature}°C, Описание: {desc}")
        else:
            st.error('{"cod":401, "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."}')
else:
    st.error('{"cod":401, "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."}')
