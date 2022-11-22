from sympy import *
import math

#author: Luis F. Diaz

x,y,z = symbols('x y z')
init_printing(use_unicode=True)

#Pseudocodigo pagina: 740 chapra modificado a iterativo
#SUB Heun (x, y, h, ynew, dydx)
 #CALL Derivs (x, y, dy1dx)
 #ye = y + dy1dx · h
 #CALL Derivs(x + h, ye, dy2dx)
 #Slope = (dy1dx + dy2dx)/2
 #ynew = y + Slope · h
 #x = x + h
#END SUB

def heun (x_, y_, xf, h, dydx):

	nc = (xf-x_)/h #numero de casos

	for i in range(int(nc)):
		print('-------------------------')
		print('ITERACION')
		print(i+1)
		#integra la funcion
		in1 =integrate(dydx, x)
		in1 =lambdify(x, in1)
		in1 = in1(x_)
		in1 =lambdify(y, in1)
		in1 = in1(y_)


		ye = y_+in1*h #Extrapolar a yᵢ+₁
		#print(ye)

		dydx_ = lambdify(x, dydx)
		dydx_ = dydx_(x_+h)
		dydx_ = lambdify(y, dydx_)
		dydx_ = dydx_(ye)


		slope = (in1+dydx_)/2 #pendiente promedio
		y_aux = y_
		y_ = y_ +slope*h
		print('Valor de y ᵢ+₁:')
		print(y_)
		x_+=h
		print('Valor de x ᵢ+₁:')
		print(x_)


heun(0, 1, 4, 0.5, -2*x**3+12*x**2-20*x+8.5)

	
	

