""" Búsqueda lineal.
 Si x está en lista devuelve su posición en lista, de lo
 contrario devuelve -1.
 """
#Función del Algoritmo: se recorren uno a uno los elementos de la lista 
#y se los compara con el valor x buscado.
def busqueda_lineal(lista, x):
 	i = 0 # i tiene la posición actual en la lista, comienza en 0
	#El ciclo recorre todos los elementos de la lista
	for z in lista:
		# estamos en la posicion i, z contiene el valor de lista[i]
		#Si z es igual a x, devuelve el valor de i
		if z == x:
			return i
		i = i+1
	#si salió del ciclo sin haber encontrado el valor, devuelve -1
	return -1
