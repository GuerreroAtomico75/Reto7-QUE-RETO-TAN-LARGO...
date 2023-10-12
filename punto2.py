n: int= 1 #Declaramos es Inicializamos la variable 'n'
iLista = [] #Creamos las listas, una para los impares y otra para los pares
pLista = []
while (n <= 1000): #Añadimos la iteración que funcionará si 'n' es menor o igual a 1000
    if (n % 2 == 1) or (n/2 == 0.5): #Usamos if para que cada vez que 'n' % 2 nos de 1 sepamos que es impar, hay una excepción y es con el 1, por eso la añadimos con el 'or'. Si n/2 = 0.5. Así se añadirá a la lista al 1
        iLista.append(n) #Cada vez que tengamos una respuesta vamos a pedir que la agregue a la lista 'ilista'
    n +=1 #Actualizamos a n más 1 para que se evaluen los demás números
    if (n % 2 == 0): #Usamos if para cada vez que tenga p % 2 sea 0 entonces será par.
        pLista.append(n) #Cada vez que tengamos una respuesta vamos a pedir que la agregue a la lista
    n += 1 #Actualizamos a n más 1 para que se evaluen los demás números
print (iLista, pLista, sep=" ; ") #Pedimos que imprima los resultados de cada lista separados.
print("Fin del ciclo") #Fin del ciclo