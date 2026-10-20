import sympy as sp
import scipy


def print_wo_point(number):
    if (number % 1 < 1e-6):
        print(int(number))
    else:
        print(number)

x = sp.symbols('x')
y = sp.sin(sp.sqrt(2*x))
x0 = 3.5
a, b = 0, 1

# 1
print('1. Значения производных 1 и 2 порядка:')
dy = sp.diff(y, x)
ddy = sp.diff(y, x,  2)
print_wo_point(sp.N(dy.subs(x, x0)))
print_wo_point(sp.N(ddy.subs(x, x0)))

# 2
print('2. Производная функции:')
sp.pprint(dy)

# 3
print('3. Значение определённого интеграла:')
def rectIntegral(a, b, n):
    result = 0
    h = (b - a) / n
  
    for i in range(n):
        result += sp.N(y.subs(x, a + h/2 + i*h))

    result *= h
    return result

print_wo_point(rectIntegral(a, b, 10000))

# 4
print('4. Неопределённый интеграл:')
Inty = sp.integrate(y, x)
sp.pprint(Inty)

# 5
def func(vars):
    x1, x2 = vars
    return (x1 + 3)**3 + (x2 - 3)**2

def constraint(vars):
    x1, x2 = vars
    return x1 - 4*x2 - 12

value = scipy.optimize.minimize(func, (0, 0), bounds=[(0, None), (0, None)], constraints={'type': 'ineq', 'fun': constraint})

print('5. Оптимальное значение функции:')
print_wo_point(value.fun)
print('Оптимальное решение:')
print_wo_point(value.x[0])
print_wo_point(value.x[1])