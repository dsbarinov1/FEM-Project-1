import streamlit as st
from PIL import Image

st.title("Математическая модель")
menu = st.sidebar.radio("*",
                        (
                         "Постановка задачи",
                         "Начальные и краевые условия",
                         )
                        )

if menu == "Постановка задачи":
    st.subheader("Постановка задачи")
    r"""
    Рассматривается математическая модель, описывающая распределение температуры при наличии фазового перехода "твердая фаза —
    жидкая фаза" при некоторой заданной температуре фазового перехода $ \ T^* $  в области  $ \Omega =  \Omega^-  \cup \Omega^+  \cup S $.
    """
    image1 = Image.open(r"Field.png")
    st.image(image1, caption = 'Рис.1. Расчетная область')
    r"""
    ### Модель Стефана
    """
    st.latex(
        r''' (\alpha(\phi) + \rho^{+} L \phi^{'})\frac{\partial T}{\partial t} - \operatorname{div} (\lambda(\phi) \operatorname {grad} \ T) = 0''')
    r"""
    $L$ -  удельная теплота фазового перехода.
    """

    """
    #### Соотношения для коэффициентов уравнения
    """
    st.latex(r''' \alpha(\phi) =  \rho^{-} c^{-} + \phi (\rho^{+} c^{+} - \rho^{-} c^{-})''')
    st.latex(r''' \lambda(\phi) =  \lambda^{-} + \phi (\lambda^{+} - \lambda^{-})''')
    st.latex(r''' \phi = \begin{cases}
                \ 0,                                                           &\quad T < T^{*} \\
                \ 1,                                                           &\quad T > T^{*} \end{cases}''')

    r"""
    где $  \rho^+, c^+  $ и $  \rho^-, c^-  $ -  плотность и удельная теплоемкость талой и мерзлой зоны, соответственно.

    
    ###
    ##### Соотношения для плотностей
    """
    
    st.latex(r''' \rho^{-} c^{-} = (1 - m) c_sc \rho_{sc} + m c_i \rho_i ''')
    st.latex(r''' \rho^{+} c^{+} = (1 - m) c_sc \rho_{sc} + m c_w \rho_w ''')
    r"""
    где $ m $ — пористость. Индексы $ sc, w, i $  обозначают соответственно каркас пористой среды, воду и лед.

    ###
    ##### Соотношения для коэфиициентов теплопроводности
    """
    st.latex(r''' \lambda^{-} = (1 - m) \lambda_{sc} + m \lambda_i ''')
    st.latex(r''' \lambda^{+} = (1 - m) \lambda_{sc} + m \lambda_w ''')
    r"""

    ###
    ##### Определение функции $\phi$ из физических соображений
    """
    st.latex(r''' \phi_\Delta (T) = \begin{cases}
                \ 0,                                                           &\quad T \leq T^{*} - \Delta,\\
                \\
                \ \frac{T - T^{*} + \Delta}{2 \Delta},         &\quad T^{*} - \Delta < T < T^{*} + \Delta \\
                \\
                \ 1,                                                           &\quad T \geq T^{*} + \Delta\end{cases}''')
    st.latex(r''' \phi^{'}_\Delta (T) = \begin{cases}
                    \ 0,                                  &\quad T \leq T^{*} - \Delta,\\
                    \\
                    \ \frac{1}{2 \Delta},         &\quad T^{*} - \Delta < T < T^{*} + \Delta \\
                    \\
                    \ 0,                                  &\quad T \geq T^{*} + \Delta\end{cases}''')
    r"""
    ###
    #### Уравнение для температуры:

    """

    st.latex(r''' (\alpha(\phi_{\Delta}) + \rho^{+} L \phi_{\Delta}^{'})\frac{\partial T}{\partial t} - div (\lambda(\phi_{\Delta}) \operatorname {grad} (T)) = 0''')



if menu == "Начальные и краевые условия":
    r"""
    ####
    ####
    ####
    #### Начальные и краевые условия
    """
    st.latex( r''' T(x, 0) = T_0,  \ \ \ \ \  x \in \Omega''')
    r"""
    ####
    ####
        """
    st.latex(r''' T(x, t) = g(x),    \ \ \ \ \       x \in Г_1''')
    st.latex(r''' -k \frac{\partial T}{\partial n} = 0,   \ \ \ \ \    x \in Г_2''')
    r"""
    ####
    где $ Γ_1 $ - место контакта с замораживающим каналом
    """