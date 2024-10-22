import random
import time

def BubbleSortt(lista):
    a = len(lista)
    if isinstance(lista, list):
        for i in range(a):
            for j in range(0, a-i-1):
                if lista[j]>lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    
        return lista
    return "ERROR"

print(BubbleSortt([1,2,4,3,7,5]))

def tiempo_promedio_ejecucion(array_tamaño, runs = 10):
    tiempo_total = 0
    for i in range(runs):
        arr = [random.randint(0, 10000) for i in range(array_tamaño)]
        iniciar_tiempo = time.time()
        BubbleSortt(arr)
        tiempo_total += time.time() - iniciar_tiempo
    return tiempo_total / runs

entradas = [1000, 2000, 3000, 4000, 5000]

tiempo_de_ejecucion = {}

for entrada in entradas:
    tiempo_de_ejecucion[entrada] = tiempo_promedio_ejecucion(entrada)

for entrada, tiempo_promedio in tiempo_de_ejecucion.items():
    print(f"Tiempo promedio para un arreglo de {entrada} elementos: {tiempo_promedio:.5f} segundos")