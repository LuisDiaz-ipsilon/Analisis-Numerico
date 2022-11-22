from sympy import *

x,y,z = symbols('x y z')
init_printing(use_unicode=True)


def euler(xi, xf, yi, h, dydx_original):
    x_=xi
    y_=yi
    nc = (xf-xi)/h #numero de casos
    print('ITERACION 0')
    print('Valor de y:')
    print(y_)
    print('Valor de x:')
    print(x_)

    for i in range(int(nc)):
        dydx = lambdify(x, dydx_original)
        dydx = dydx(x_)
        dydx = lambdify(y, dydx)
        dydx = dydx(y_)
        y_aux = y_
        y_ = y_+dydx*h
        x_ = x_+h
        print('-------------------------')
        print('ITERACION ')
        print(i+1)
        print('Valor de y:')
        print(y_)
        print('Valor de x:')
        print(x_)
        dydx = dydx_original
        err = abs((y_ -y_aux)/y_)*100
        print('Error relativo porcentual:')
        print(err)

euler(0, 4, 1, 0.5, -2*x**3+12*x**2-20*x+8.5)
