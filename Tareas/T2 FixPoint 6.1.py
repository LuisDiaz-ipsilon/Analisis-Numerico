import math


#input F(x), _Ea: error esperado, _Es: Error maximo, Xl, Xu

#--------------------------------Establer valores de variable
def F(x):
	return ((math.e)**-x)-x

#Entonces g(x):
def G(x):
	return 2*(math.sin(math.pow(x, 1/2)))


_Es=00.001 #Error Aproximado maximo
X0 = 0.5
#--------------------------
_Ea=00.00 #Error Aproximado
Xr=0
i=0
Xrold=0
Xr=X0


#------------------ EJECUCION

while (True) :
	Xrold = Xr
	Xr = G(Xrold)
	i=i+1
	if Xr!=0 :
		_Ea = abs((Xr-Xrold)/Xr)*100
	print('Error aproximado: (Ea)%')
	print(_Ea)
	print('Posible raiz verdadera: (Xr)')
	print(Xr)
	print('\n')
	if _Ea< _Es:
		break