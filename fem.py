import fenics
from dolfin import *
from ufl import coefficient

mesh = Mesh("rock.xml")
boundaries = MeshFunction('size_t', mesh, "rock_facet_region.xml")

DAY = 86400
timestep = 0.1 * DAY
rhol = 6.0e7
cros = 2.0e6
crol = 2.5e6
kS = 1.8
kL = 2.0
delta = 1.0
sou = -30.0
initT = 2.0

V = FunctionSpace(mesh, 'Lagrange', 2)

U = TrialFunction(V)
v = TestFunction(V)
T0  = Function(V)

bc = DirichletBC(V, sou, boundaries, 1)

tau = Constant(timestep)
rhol = Constant(rhol)
cros = Constant(cros)
crol = Constant(crol)
kS = Constant(kS)
kL = Constant(kL)
delta = Constant(delta)

initT = Constant(initT)

phi = conditional(gt(T0, delta), 1.0, conditional(lt(T0, -delta), 0.0, (T0+delta)/(delta+delta) ))
dphi = conditional(gt(T0, delta), 0.0, conditional(lt(T0, -delta), 0.0, 1.0/(delta+delta) ))
k = kS + phi*(kL - kS)
cro = cros + phi*(crol - cros)
a = (cro + rhol*dphi) * U/tau*v*dx + inner(k * grad(U), grad(v))*dx
L = (cro + rhol*dphi)*T0/tau*v*dx

T = Function(V)
T0.interpolate(initT)
path = 'results1/'

T_file = File(f'{path}t.pvd')

for t in range (0, 60*DAY, int(timestep)):
    solve(a == L , T, bc)
    T0.assign(T)
    T_file << (T, t)
