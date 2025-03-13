import streamlit as st
import requests

# Ваш API-ключ OpenWeatherMap
API_KEY = 'ваш_ключ_API'

# Функция для получения данных о погоде
def get_weather(city):
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Градусы Цельсия
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Основная часть приложения Streamlit
st.title("Погодное приложение")  # Заголовок

# Создаем выпадающий список для выбора города
city = st.selectbox("Выберите город:", ['London', 'New York', 'Tokyo', 'Moscow', 'Madrid'])

# Кнопка для получения погоды
if st.button("Получить погоду"):
    weather_data = get_weather(city)
    if weather_data:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        st.success(f"Температура в {city}: {temperature}°C, Описание: {description}")
    else:
        st.error("Не удалось получить данные о погоде. Убедитесь, что город введен правильно.")
