paisA : float = 25 #Declaramos y inicializamos variables con los datos del problema
paisB : float = 18.3
crecimientoPaisA = [] #Crearemos una lista que en principio estará vacía porque los datos iniciales del ejercicio son los del año 0
crecimientoPaisB = []
while paisA > paisB: # Crearemos una iteración que se usará mientras el país A tenga más población que el país B
    def calcularCrecimientoPoblacionalPaisA (paisA : float) -> float: #Creamos una función en la que se calcule el crecimiento del país A cada año
        porcentajeA = paisA * 0.02 #Primero multiplicamos la población del país por el 2%
        aumentoPoblacionalA = porcentajeA + paisA #El resultado dado lo sumamos a la población de ese momento del país
        return aumentoPoblacionalA

    def calcularCrecimientoPoblacionalPaisB (paisB : float) -> float: #Creamos una función en la que se calcule el crecimiento del país B cada años
        porcentajeB = paisB * 0.03 #Primero multiplicamos la población del país por el 3%
        aumentoPoblacionalB = porcentajeB + paisB #El resultado dado lo sumamos a la población de ese momento del país
        return aumentoPoblacionalB
    
    if __name__ == "__main__":
        poblacionA = calcularCrecimientoPoblacionalPaisA(paisA) #Tenemos las funciones
        poblacionB = calcularCrecimientoPoblacionalPaisB(paisB)
        crecimientoPaisA.append(poblacionA) #Estos resultados los agregamos a la lista
        crecimientoPaisB.append(poblacionB)
        
    paisA += (poblacionA - paisA) #Actualizamos la población del país, Será la resta de la población al aumentar porcentualmente menos la población que estaba

    paisB += (poblacionB - paisB) #Actualizamos la población del país, Será la resta de la población al aumentar porcentualmente menos la población que estaba

    añoActual = len(crecimientoPaisA) + 2022 #Sumamos la cantidad de elementos de una de las dos listas más el año 2022

    #Si quisieramos ver más a detalle cuando se aumentó poblacionalmente el ejercicio entonces tener en cuenta:
    #print(crecimientoPaisA, crecimientoPaisB, sep="; ")

print("En el año", añoActual,"el pais B supera al pais A poblacionalmente, teniendo en cuenta que se inició la comparación en el 2022") #Esta será la respuesta en que año el país B supera al pais A
print("Fin de Ciclo")
