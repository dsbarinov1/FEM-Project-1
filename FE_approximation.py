import streamlit as st

st.title("Конечно-элементная аппроксимация")
r"""
#####
####
Проведем аппроксимацию по пространству задачи с использованием метода конечных элементов. Умножим уравнение для температуры на тестовую функцию v и проинтегрируем с использованием формулы Грина:
"""
st.latex(
    r''' \int_\Omega (\alpha(\phi_\bigtriangleup) + \rho_l L \phi_\bigtriangleup^{'}) \frac{\partial T}{\partial t} v \; \mathrm{d}x  + \int_\Omega (\lambda(\phi_\bigtriangleup) \operatorname {grad} \ T, \operatorname {grad} \ v) \; \mathrm{d}x = 0''')
st.latex(r''' v     \in \^{V} =  \{ v \in H_1(Ω) : v |_{Г_1} = 0 \} ''')
st.latex(r''' T     \in V =  \{ v \in H(Ω) : v |_{Г_1} = g \} ''')
r"""
#####
где $ H(Ω) $ - пространство Соболева, состоящее из функций $ v $ таких, что $ v^2 $ и $ |∇v|^2 $ имеют конечный интеграл в $ Ω $.
Для простоты, определим равномерную сетку по времени
"""
st.latex(r''' \omega_{\tau} =  \{ t^n = n \cdot \tau, n = 0, 1, ..., N_0, \tau N_0 = t_{max} \} ''')

r"""
#####
и проведем аппроксимацию по времени с использованием стандартной чисто неявной схемы. Для нелинейного уравнения воспользуемся
простейшей линеаризацией, когда коэффициенты зависят от значения функции с предыдущего временного слоя:

"""
st.latex(
r''' \int_\Omega (\alpha(\phi_\bigtriangleup^{n}) + \rho_l L \phi_\bigtriangleup^{'n}) \frac{T^{n+1} - T^n}{\tau} v \; \mathrm{d}x  + \int_\Omega (\lambda(\phi_\bigtriangleup^{n}) \operatorname {grad} T^{n+1}, \operatorname {grad} v) \; \mathrm{d}x = 0''')
r"""
#####
где $ T^n = T(t^n)  ∈ V $
Для численного решения мы должны перейти от непрерывной вариационной задачи к дискретной. Введем конечномерные пространства $ V_h ⊂ V , \^{V_h} ⊂ \^{V} $ и определим в них следующую задачу:
найти $ T_h ∈ V_h $ такую что
"""
st.latex(
r''' \int_\Omega (\alpha(\phi_\bigtriangleup^{n}) + \rho_l L \phi_\bigtriangleup^{'n}) \frac{T_h^{n+1} - T_h^n}{\tau} v \; \mathrm{d}x  + \int_\Omega (\lambda(\phi_\bigtriangleup^{n}) \operatorname {grad} T_h^{n+1}, \operatorname {grad} v) \; \mathrm{d}x = 0, \forall v_h \ni \hat{V_h}''')
r"""
#####
 выбор пространства $\^{V_h}$ непосредственно вытекает из типа применяемых конечных элементов.
"""
