n : int = int(input("Ingrese cualquier número entero: ")) #Declaramos e inicializamos la variable pidiendole a la persona que ingrese un número entero.
pLista = [] # Creamos la lista 'pLista' que es la que se va a imprimir al final
while n >= 2: #Hacemos una iteración que funcionará siempre que se tenga un número mayor o igual a 2
    if n % 2 == 0: #Si el número es par entonces se agregará a la lista
        pLista.append(n)
    n -= 1 #Actualizamos restandole a 'n' -1
    if n % 2 == 1: #Si el número es impar entonces simplemente actualizamos 'n'-1
        n -= 1
print(pLista) # Imprimimos la lista 'pLista' que es donde estarán los enteros
print("Fin del ciclo") #Si ya se acaba la iteración se finaliza el ciclo