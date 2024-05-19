import streamlit as st

r"""
# Визуализация численного моделирования промерзания грунта.
##### Интервал времени: 30 (дней). 
##### Шаг расчета: 10.
##### Всего: 300 шагов по времени.
"""
video_file = open('anime.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)