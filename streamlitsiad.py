import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Погодное приложение Сиад Кнад")
file= st.file_uploader("Выберите файл с датасетом погоды", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.write("Содержимое вашего файла:")
    st.dataframe(df)
with st.form('forma'):
    akey = st.text_input("Введите ваш API-key:")
    submit_b = st.form_submit_button("Сохранить")
city = st.selectbox("Выберите город:", ['London', 'New York', 'Tokyo', 'Moscow', 'Paris','Sydney', 'Berlin','Beijing','Rio de Janeiro','Dubai','Los Angeles','Singapore','Mumbai','Cairo','Mexico City'])
if akey and file is not None:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={akey}&units=metric"
    if st.button("Получить погоду"):
        request = requests.get(url)
        datatext = request.json()
        if datatext:
            temperature = datatext['main']['temp']
            cursis = df[df['city'] == city]['season'].mode()[0]
            season_data = df[df['season'] == cursis]
            normm = season_data['temperature'].mean()
            norms = season_data['temperature'].std()            
            diapason = (normm - 2 * norms, normm + 2 * norms)
            if diapason[0] <= temperature  and temperature <= diapason[1]:
                st.success(f"Температура в {city}: {temperature}°C Нормальная для текущего сезона!")
            else:
                st.warning(f"Температура в {city}: {temperature}°C - Аномальная для текущего сезона!")
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=season_data, x='timestamp', y='temperature', label='Temperature')
            sns.scatterplot(data=season_data[season_data['anomalies']], x='timestamp', y='temperature', color='red', label='Anomalies')
            plt.axhline(y=normm + 2 * norms, color='r', linestyle='--', label='Upper Bound')
            plt.axhline(y=normm - 2 * norms, color='r', linestyle='--', label='Lower Bound')
            plt.title(f'Временной ряд температуры в {city}')
            plt.xlabel("Дата")
            plt.ylabel("Температура (°C)")                
            plt.legend()
            st.pyplot(plt)
            
        else:
            st.error('{"cod":401, "message": "Invalid API key. Please see https://openweathermap.org/faq#error401 for more info."}')
    
