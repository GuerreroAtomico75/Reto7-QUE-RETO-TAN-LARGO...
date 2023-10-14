import random #Importamos la bibloteca random

numero = int(input("Ingrese un número que usted piense de 1 a 100: ")) #Le pedimos al usuario que ingrese un número que él esté pensando de 1 a 100
numeroMaximo = 100 #Ponemos un número máximo que en este caso sera el 100
numeroMinimo = 1 # Ponemos un número mínimo que en este caso será el 1

while 1 <= numero <= 100: #Creamos iteración que funcionará mientras 'numero' esté entre 1 y 100
    numeroRandom=random.randint(numeroMinimo, numeroMaximo) #Haremos que el programa genere un número random con .randint, diciendole que ese número esté entre el número mínimo y el número máximo
    print("¿El número", numeroRandom, "es el que pensó? Puede responder de la siguiente manera: 'mayor', 'menor' o 'igual'") #Le preguntaremos al usuario si el número que generó fue el que usted pensó. Le damos las opciones de respuesta que puede dar
    rta = input("Ingrese su respuesta: ") #Hacemos que el usuario responda y dependiendo de su respuesta sucederá lo siguiente
    if rta == 'mayor': #Si su respuesta es que el número que él pensó es mayor entonces responderá 'mayor' y... 
        numeroMinimo = numeroRandom + 1 # ... actualizamos al número mínimo sumándole al número random un 1
    elif rta == 'menor': #Si su respuesta es que el número que él pensó es menor entonces responderá 'manor' y...
        numeroMaximo = numeroRandom - 1 # ... actualizamos al número máximo restándole al número random un 1
    elif rta == 'igual': # Si su respuesta es 'igual' entonces ...
        break # Rompemos la iteración
print("El", numeroRandom, "fue el que usted pensó") #Imprimimos el número que la persona pensó
print("Fin de la iteración") #Fin de la iteración