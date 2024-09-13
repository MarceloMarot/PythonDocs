#Busqueda de todos los numeros primos entre 1 y un numero máximo
import time
from numba import jit
import sys


# version interpretada
def numeros_primos(numero_maximo):
    """Devuelve una lista con los numeros primos encontrados con valor menor al indicado."""""
    #esta funcion verifica qué numeros son primos descartando los numeros divisibles por enteros previos
    #los numeros primos se guardan en una lista
    primos = [2]
    #se prueba cada numero candidato, uno a uno
    #sólo se verifican numeros impares: mejora casi imperceptible
    for valor in range(3,numero_maximo+1,2):
        divisible = False
        # sólo se divide por numeros primos ya encontrados 
        # los numeros no primos son redundantes
        for indice in range(0,len(primos)):
            divisor = primos[indice]
            if valor % divisor == 0:
                divisible = True
                break
        #si no es divisible se cuenta como primo
        if divisible == False:
            primos.append(valor)
    return primos     


# version compilada en ejecucion
@jit        # decorador de Numba
def numeros_primos_compilado(numero_maximo):
    """Devuelve una lista con los numeros primos encontrados con valor menor al indicado."""""
    #esta funcion verifica qué numeros son primos descartando los numeros divisibles por enteros previos
    #los numeros primos se guardan en una lista
    primos = [2]
    #se prueba cada numero candidato, uno a uno
    #sólo se verifican numeros impares: mejora casi imperceptible
    for valor in range(3,numero_maximo+1,2):
        divisible = False
        # sólo se divide por numeros primos ya encontrados 
        # los numeros no primos son redundantes
        for indice in range(0,len(primos)):
            divisor = primos[indice]
            if valor % divisor == 0:
                divisible = True
                break
        #si no es divisible se cuenta como primo
        if divisible == False:
            primos.append(valor)
    return primos     
  




if __name__ == "__main__":

    valor_maximo = int(sys.argv[1])

    # repeticiones test
    n = 3

    print("=============== Tiempos ejecucion ========================")

    tiempo           = []
    tiempo_compilado = []

    for i in range(n):

        inicio  = time.time()
        valores = numeros_primos( valor_maximo )
        fin     = time.time()
        t = fin - inicio 
        tiempo.append(t)

        inicio  = time.time()
        valores = numeros_primos_compilado( valor_maximo )
        fin     = time.time()
        t = fin - inicio 
        tiempo_compilado.append(t)

        print(f"Interpretado: {int(tiempo[i]*1e3):6} mseg , compilado: {int(tiempo_compilado[i]*1e3):6} mseg")







