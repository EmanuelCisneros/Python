#Este es el vector que el algoritmo usara para buscar cualquier dato
vector = [3, 5, 8, 9, 10, 22, 45, 500, 900, 4253]
#La variable puntero sera el inicio del vector, que es 0
puntero = 0
#vectorLen contiene la longitud del vector
vectorLen = len(vector)
#La varieable encontrado cambiara su valor, y asi el algoritmo sabre que hacer luego
encontrado = False

#Le pedimos al usuario una entrada de un entero
numero = int(input("Ingresar el dato que desea buscar: "))

#Creamos un bucle que no se detenga hasta que encontrado sea diferente de False
#Y que puntero sea menor o igual que vectorLen
while not(encontrado) and puntero <= vectorLen:
	#Creamos la variable mitad
	mitad = int((puntero+vectorLen) / 2)
	#Si numero es igual que el indice mitad en vector
	if numero == vector[mitad]:
		#Encontado sera igual a True
		encontrado = True
	#De lo contrario, si el indice mitad en vector es menor que numero
	elif numero < vector[mitad]:
		#vectorLen sera igual que mitad - 1
		vectorLen = mitad - 1
	#De lo contrario
	else:
		#Puntero sera igual que mitad + 1
		puntero = mitad + 1
#Si encontrado es True
if(encontrado):
	#MOstramos un mensaje con la posicion del Dato en el vector
	print("El dato se encuentra en la posicion ", str(mitad+1))
	#Mostramos el vector ordenado
	print(vector)
#De lo contrario
else:
	#Mostramos un mensaje avisandole al usuario que el dato ingresado no se encuentra dentro del vector
	print("El dato no se encontro")