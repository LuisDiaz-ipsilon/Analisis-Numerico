import math


#input F(x), _Ea: error esperado, _Es: Error maximo, Xl, Xu

#--------------------------------Establer valores de variable
def F(x):
	return ((math.e)**-x)-x


_Es=05.00 #Error Aproximado maximo
Xl = 0 
Xu = 1
#--------------------------
_Ea=00.00 #Error Aproximado
Xr=0
i=0
Xrold=0
exit = False
fl=F(Xl)
fu=F(Xu)
il=0
iu=0

#Validacion de valores a la derecha e izquierda de la raiz que buscamos
if(F(Xl)*F(Xu)>0.0):
	print('Deben acotar por la izquierda y derecha la raiz')
	exit = True


while (exit == False):
	Xrold = Xr
	Xr = Xu-fu*(Xl-Xu)/(fl-fu)
	fr=F(Xr)
	i=i+1
	print('-------Itereacion: ')
	print(i)
	if Xr!=0:
		_Ea = abs((Xr-Xrold)/Xr)*100
	test = fl*fr
	if test < 0:
		Xu=Xr
		fu=F(Xu)
		iu=0
		il=il+1
		if il >= 2:
			fl=fl/2
	elif test > 0:
		xl = Xr
		fl = F(Xl)
		il = 0
		iu = iu + 1
		if iu>=2 :
			fu=fu/2
		else:
			_Ea = 0
	

	print('Error aproximado: (Ea)%')
	print(_Ea)
	print('Posible raiz verdadera: (Xr)')
	print(Xr)
	print('\n')
	if _Ea < _Es:
			exit = True
	