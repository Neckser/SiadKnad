import streamlit as st
import requests

st.title("Погодное приложение")

with st.form(key='my_form'):
    akey = st.text_input("Введите ваш API-key:") 
    submit_button = st.form_submit_button(label='Отправить')
city = st.selectbox("Выберите город:", ['London', 'New York', 'Tokyo', 'Moscow', 'Madrid'])
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
