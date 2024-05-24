import streamlit as st
from PIL import Image

st.title("Расчетная сетка")

r"""
Создадим геометрию тела (на языке Gmsh). Зададим точки геометрии:
"""

code = r"""
// Гиперпараметры
L = 2;
r = 0.1;
p1 = L/30;
p2 = r/5;

// Точки границ
Point(1) = {0, 0, 0, p1}; // левая нижняя
Point(2) = {L, 0, 0, p1}; // правая нижняя
Point(3) = {L, L, 0, p1}; // правая верхняя
Point(4) = {r, L, 0, p2}; //левая верхняя
Point(5) = {r, L/2, 0, p2}; // конец отрезка под стержнем
Point(6) = {0, L/2, 0, p2}; // начало отрезка под стержнем
"""
st.code(code)
st.image("mesh_points.png", caption = 'Рис.1. Добавление точек')

r"""
Соединим точки линиями:
"""
code1 = r"""
// Линии границ
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 6};
Line(6) = {6, 1};
"""
st.code(code1)
st.image("mesh_lines.png", caption = 'Рис.2. Добавление линий границ')

r"""
Создадим замкнутый контур тела и поверхность. Затем выделим физические группы и создадим сетку:
"""
code2 = r"""
// Замкнутый контур
Line Loop(7) = {1, 2, 3, 4, 5, 6};

// Поверхность
Plane Surface(8) = {7};

// Выделяем физические группы
Physical Line(1) = {4, 5}; // группа границ стержня
Physical Line(2) = {3, 6, 1, 2}; // группа оставшихся границ
Physical Surface(1) = {8}; // группа поверхностей

// Создаем двумерную сетку
Mesh 2;

"""

st.code(code2)

r"""
##### Итоговая расчетная сетка:
"""
st.image("fe_mesh.png", caption = 'Рис.3. Расчетная сетка')