from sympy import *

x,y,z = symbols('x y z')
init_printing(use_unicode=True)

#Pseudocodigo pagina: 740 chapra
#SUB Heun (x, y, h, ynew, dydx)
 #CALL Derivs (x, y, dy1dx)
 #ye = y + dy1dx · h
 #CALL Derivs(x + h, ye, dy2dx)
 #Slope = (dy1dx + dy2dx)/2
 #ynew = y + Slope · h
 #x = x + h
#END SUB

def heun (x_, y_, h, ynew, dydx):

	#Deriva la funcion
	d1 =diff(dydx, x)
	d1 =lambdify(x, d1)
	d1 = d1(x_)
	d1 =lambdify(y, d1)
	d1 = d1(y_)

	ye = y_+d1*h #Extrapolar a yᵢ+₁

	d2 = diff(dydx, x)
	d2 = lambdify(x, d2)
	d2 = d2(x_+h)
	d2 = lambdify(y, d2)
	d2 = d2(ye)

	slope = (d1+d2)/2 #pendiente promedio
	ynew = y_ +slope*h
	print('-------------------------')
	print('Valor de y ᵢ+₁:')
	print(ynew)
	x_=x_+h
	print('-------------------------')
	print('Valor de x ᵢ+₁:')
	print(x_)

	Et=abs(ynew-y_)/ynew*100
	print('-------------------------')
	print('Error relativo porcentual:')
	print(Et)

heun(0, 1, 0.5, 0, x*2*y**3)

	
	

