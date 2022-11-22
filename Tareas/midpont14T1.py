from sympy import *
import math

#author: Luis F. Diaz

x,y,z = symbols('x y z')
init_printing(use_unicode=True)

def midpoint (x_, y_, xf, h, dydx):

	nc = (xf-x_)/h #numero de casos

	for i in range(int(nc)):
		print('-------------------------')
		print('ITERACION')
		print(i+1)
		#integra la funcion
		d1 =diff(dydx, x)
		d1 =lambdify(x, d1)
		d1 = d1(x_)
		d1 =lambdify(y, d1)
		d1 = d1(y_)


		ym = y_+d1*h #Extrapolar a yᵢ+₁

		dydxm = diff(dydx, x)
		dydxm = lambdify(x, dydx)
		dydxm = dydxm(x_+(h/2))
		dydxm = lambdify(y, dydxm)
		dydxm = dydxm(ym)

		y_ = y_ +dydxm*h
		print('Valor de y ᵢ+₁:')
		print(y_)
		x_+=h
		print('Valor de x ᵢ+₁:')
		print(x_)


midpoint(0, 2, 4, 1, 4*(math.e**0.8*x)-0.5*y)

	
	

