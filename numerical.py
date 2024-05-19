import streamlit as st

st.title("Численная реализация")

r"""
##### Загрузка сетки и границ области
"""
code1=r"""
mesh = Mesh("rock.xml")
boundaries = MeshFunction('size_t', mesh, "rock_facet_region.xml")
"""
st.code(code1, language="python")
st.write("---")

r"""
##### Задание параметров
"""
code2 = r"""
DAY = 86400
timestep = 0.5 * DAY
rhol = 6.0e7
cros = 2.0e6
crol = 2.5e6
kS = 1.8
kL = 2.0
delta = 1.0
sou = -30.0
initT = 2.0
"""
st.code(code2, language="python")
st.write("---")

r"""
##### Задание функционального пространства (выбор Лагранжевых конечных элементов)
"""
code3 = r"""
V = FunctionSpace(mesh, 'Lagrange', 1)
"""
st.code(code3, language="python")
st.write("---")

r"""
##### Выбор пробных и тестовых функций
"""
code4=r"""
U = TrialFunction(V)
v = TestFunction(V)
T0  = Function(V)
"""
st.code(code4, language="python")
st.write("---")

r"""
##### Задание граничных условий Дирихле
"""
code5=r"""
bc = DirichletBC(V, sou, boundaries, 1)
"""
st.code(code5, language="python")
st.write("---")

r"""
##### Преобразование констант
"""
code6=r"""
tau = Constant(timestep)
rhol = Constant(rhol)
cros = Constant(cros)
crol = Constant(crol)
kS = Constant(kS)
kL = Constant(kL)
delta = Constant(delta)

initT = Constant(initT)
"""
st.code(code6, language="python")
st.write("---")

r"""
##### Задание функций из уравнения
"""
code7=r"""
phi = conditional(gt(T0, delta), 1.0, conditional(lt(T0, -delta), 0.0, (T0+delta)/(delta+delta) ))
dphi = conditional(gt(T0, delta), 0.0, conditional(lt(T0, -delta), 0.0, 1.0/(delta+delta) ))
k = kS + phi*(kL - kS)
cro = cros + phi*(crol - cros)
a = (cro + rhol*dphi) * U/tau*v*dx + inner(k * grad(U), grad(v))*dx
L = (cro + rhol*dphi)*T0/tau*v*dx

T = Function(V)
"""
st.code(code7, language="python")
st.write("---")

r"""
##### Задание начальных условий
"""
code8=r"""
T0.interpolate(initT)
"""
st.code(code8, language="python")
st.write("---")

r"""
##### Расчет и выгрузка результатов
"""
code9=r"""
path = 'results1/'
file = open("rezult.txt","w+")
T_file = File(f'{path}t.pvd')

for t in range (0, 30*DAY, int(timestep)):
    solve(a == L , T, bc)
    T0.assign(T)
    T_file << (T, t)
"""
st.code(code9, language="python")
st.write("---")
