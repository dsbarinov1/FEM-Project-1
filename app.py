import streamlit as st
from st_pages import Page, show_pages



st.set_page_config(layout="wide")
st.sidebar.title("Ссылки на технологии:")
st.sidebar.link_button("FEniCS project", "https://fenicsproject.org/")
st.sidebar.link_button("Gmsh", "https://gmsh.info/")

st.sidebar.title("Ссылки на технологии:")
st.sidebar.link_button("Github проекта №1", "https://streamlit.io/gallery")
st.sidebar.link_button("Github проекта NumPy", "https://streamlit.io/gallery")
st.sidebar.link_button("Github проекта Gmsh", "https://streamlit.io/gallery")

show_pages(
    [
        Page("app.py", "Заглавие", "🏠"),
        Page("goals.py", "Цель и задачи"),
        Page("math_model.py", "Математическая модель"),
        Page("FE_approximation.py", "Конечно-элементная аппроксимация"),

    ]
)

st.title("Проект №1: Теплоперенос в грунте при наличии фазовых переходов")
st.write("\n  ")
st.write("\n  ")
st.write("\n  ")
st.write("\n  ")

col1, col2 = st.columns(2)

with col1:
    st.image("fenics.png")

with col2:
    st.image("gmsh.png", width=250)

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n  ")
st.write("\n  ")



c1, c2 = st.columns((1, 1))

with c1:
    st.subheader("**Работу выполнили студенты МГУ Саров из группы ВМ-123    :**")

with c2:
    st.subheader("Бабенко Михаил, Баринов Даниил")
    st.subheader("Гайсин Роберт, Кислер Роман")