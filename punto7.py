n = int(input("Ingrese un número entero del 2 al 50: ")) #Le pedimos al usuario que ingrese un el número el cual el quiere saber sus divisores. Este número debe estar entre 2 y 50
d = 1 # 'd' va a ser el denominador de la división que se hará con 'n'.
divisoresLista = [] # Creamos una lista para que los divisores entren en esa lista

while n >= d: #Ponemos iteración siempre que 'n' sea mayor o igual a 'd'
    #Ponemos condicionales para los casos que pueden ocurrir
    if n%d == 0: #EL primer caso será que si n%d es igual a 0 entonces es divisor
        divisoresLista.append(d) # Si es así añadimos a la lista
        d += 1 # Sumamos 1 a d
    else: # Sino solo sumamos 1 a d
        d += 1
print("Los devisores de", n, "son", divisoresLista) # Ya cuando se termina la iteración nos votará los divisores de n.