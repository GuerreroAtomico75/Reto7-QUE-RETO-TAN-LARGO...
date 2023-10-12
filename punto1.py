n : int = 1 #Declaramos e inicializamos la variable
while n <= 100: #Aplicamos iteración
    cuadrado = n**2 #aplicamos num al cuadrado
    print (n, cuadrado, sep=", ") #Imprimimos el num, el cuadrado del num y los separamos con sep=
    n += 1 #Actualizamos +1 para que se evaluen los demás enteros posibles
print("Fin del ciclo") #Si la respuesta booleana de la iteración no es verdadera se acaba el ciclo e imprime 'fin de ciclo'