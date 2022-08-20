#Tarea 2 metodo biseccion para el problema 5.15
#Autor: Luis Fernando Flores Diaz 1821936

import math


#input F(x), _Ea: error esperado, _Es: Error maximo, Xl, Xu

#--------------------------------Establer valores de variable
def F(x):
	return 1-((400/(9.81*(3*x+((x*x)/2))**3))*(3+x))



_Es=01.00 #Error Aproximado maximo
Xl = 0.5 
Xu = 2.5



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




