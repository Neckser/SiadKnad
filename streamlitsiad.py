import streamlit as st
import requests

st.title("Погодное приложение")

city = st.selectbox("Выберите город:", ['London', 'New York', 'Tokyo', 'Moscow', 'Madrid'])

if st.button("Получить погоду"):
    request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b996270006c7d6e003daadb143d5ae39&units=metric")
    weather_data = request.json()
    if weather_data:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        st.success(f"Температура в {city}: {temperature}°C, Описание: {description}")
    else:
        st.error('{"cod":401, "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."}')
