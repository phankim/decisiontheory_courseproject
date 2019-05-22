from cvxopt import matrix, solvers

c = matrix([-1, -1, 0, 0, -1, -1, -1, 0, -1], tc='d') #Целевая функция (минусы, потому что решаем задачу максимизации) 
G = matrix([[0.006, 0.008,  0,  0, 0.006, 0.004, 0.005,  0, 0.002],   # Коэффициенты при ограничениях-неравенствах (вида <=)
            [   12,     8,  0,  0,     0,     0,     0,  0,     0],
            [    0,     0,  0,  0,     6,    15,     0,  0,     0],
            [    0,     0,  0,  0,     0,     0,    12,  0,    19],
            [    1,    -1,  0,  0,     1,     0,    -1,  0,     0],
            [    0,     1,  0,  0,     1,    -1,     0,  0,    -1],
            [   -1,     0,  0,  0,     0,     0,     0,  0,     0],
            [    0,    -1,  0,  0,     0,     0,     0,  0,     0],
            [    0,     0, -1,  0,     0,     0,     0,  0,     0],
            [    0,     0,  0, -1,     0,     0,     0,  0,     0],
            [    0,     0,  0,  0,    -1,     0,     0,  0,     0],
            [    0,     0,  0,  0,     0,    -1,     0,  0,     0],
            [    0,     0,  0,  0,     0,     0,    -1,  0,     0],
            [    0,     0,  0,  0,     0,     0,     0, -1,     0],
            [    0,     0,  0,  0,     0,     0,     0,  0,    -1]], tc='d')
h = matrix([48,87000,52200,69000,0,0,0,0,0,0,0,0,0,0,0], tc='d')
solution = solvers.lp(c, G.T, h, solver='glpk')
print('Status:', solution['status'])
print('Objective:', solution['primal objective'])
print('x = \n', solution['x'])
print(solution['z'])
# Исследование интервала осуществимости 
dh = matrix([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);     # приращение к вектору правых частей
solution1 = solvers.lp(c, G.T, h + dh, solver='glpk')
print('Status:', solution1['status'])
print('Objective:', -solution1['primal objective'], 'delta:', -solution1['primal objective']-(-solution['primal objective']))
print(solution1['x'])

prev_z= -solution['primal objective']
a = 1
while (True):
    solution_i= solvers.lp(c, G.T, h + dh*a, solver='glpk')
    if solution_i['status'] != 'optimal':
        print('Couldn''t find a solution')
        break
    new_z= -solution_i['primal objective']
    delta_z= new_z-prev_z
    print('Increment %d: obj=%.2f delta=%.2f' % (a, new_z, delta_z))
    if abs(delta_z-1200) > 1e-6:
        print('Basis changed at increment %d' % (a,))
        break
    prev_z = new_z
    a = a + 1
