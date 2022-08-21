#Tarea 1 metodo biseccion 
#Autor: Luis Fernando Flores Diaz 1821936

import math


#input F(x), _Ea: error esperado, _Es: Error maximo, Xl, Xu

#--------------------------------Establer valores de variable
def F(x):
	return -0.874*(x**2)+1.65*x+2.627



_Es=05.00 #Error Aproximado maximo
Xl=2.9
Xu=3.1


#--------------------------
_Ea=00.00 #Error Aproximado
Xr=0
i=0
Xrold=0
exit = False

#-----------------------------------EJECUCION----------------------

#Outpud sera : Xr
while(exit == False) :
	Xrold = Xr
	Xr = (Xl+Xu)/2
	i=i+1
	print('-------Itereacion: ')
	print(i)
	if(Xr!=0):
		_Ea = abs(Xr-Xrold)/Xr*100
	
	test = F(Xl)*F(Xr)
	if(test<0): 
		Xu=Xr
		#print('Xu toma el valor de Xr')
	elif test>0:
		Xl=Xr
		#print('Xl toma el valor de Xr')
	else :
		_Ea = 0
		print('La raiz es Xr')
		print(Xr)

	if _Ea<_Es:
		exit = True


	print('Error aproximado: (Ea)%')
	print(_Ea)
	print('Posible raiz verdadera: (Xr)')
	print(Xr)
	print('\n')




