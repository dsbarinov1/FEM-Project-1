import streamlit as st
from PIL import Image

st.title("Конечно-элементная аппроксимация")
st.latex(
    r''' \int\limits_\Omega (\alpha(\phi_\bigtriangleup) + \rho_l L \phi_\bigtriangleup^{'}) \frac{\partial T}{\partial t} v \; \mathrm{d}x  + 
    \int\limits_\Omega \lambda(\phi_\bigtriangleup) \operatorname {grad}T \, \operatorname {grad}v \; \mathrm{d}x = 0''')
st.latex(r''' v     \in V_0=  \{ v \in H^1(\Omega) : v |_{Г_1} = 0 \} ''')
st.latex(r''' T     \in V_D =  \{ v \in H^1(\Omega) : v |_{Г_1} = g \} ''')
r"""
#####

#### Равномерная сетка по времени
"""
st.latex(r''' \omega_{\tau} =  \{ t^n = n \, \tau, \; n = 0, 1, ..., N_0, \; \tau N_0 = t_{max} \} ''')

r"""
#####
#### Неявная схема с линеаризацией

"""
st.latex(
r''' \int\limits_\Omega (\alpha(\phi_\bigtriangleup^{n}) + \rho_l L \phi_\bigtriangleup^{'n}) \frac{T^{n+1} - T^n}{\tau} v \; \mathrm{d}x  + 
\int\limits_\Omega \lambda(\phi_\bigtriangleup^{n}) \operatorname {grad} T^{n+1} \, \operatorname {grad} v \; \mathrm{d}x = 0''')
r"""
#####
где $ T^n = T(t^n)  \in V_D $


#### Конечно-элементная аппроксимация
Введем конечномерные пространства $ V_{0,h} \subset V_0 , V_{D,h} \subset V_{D} $ и определим в них следующую задачу:
найти $ T_h \in V_{D,h} $ такую что
  """
st.latex(
    r''' \int\limits_\Omega (\alpha(\phi_\bigtriangleup^{n}) + \rho_l L \phi_\bigtriangleup^{'n}) \frac{T_h^{n+1} - T_h^n}{\tau} v \; 
    \mathrm{d}x  + \int\limits_\Omega \lambda(\phi_\bigtriangleup^{n}) \operatorname {grad} T_h^{n+1} \, \operatorname {grad} v \; 
    \mathrm{d}x = 0, \; \forall v_h \ni V_{0,h}''')