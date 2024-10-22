import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivot]
    medio = [x for x in arr if x == pivot]
    derecha = [x for x in arr if x > pivot]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

def tiempo_promedio_ejecucion(array_tamaño, runs = 10):
    tiempo_total = 0
    for i in range(runs):
        arr = [random.randint(0, 10000) for i in range(array_tamaño)]
        iniciar_tiempo = time.time()
        quick_sort(arr)
        tiempo_total += time.time() - iniciar_tiempo
    return tiempo_total / runs

entradas = [1000, 2000, 3000, 4000, 5000]

tiempo_de_ejecucion = {}

for entrada in entradas:
    tiempo_de_ejecucion[entrada] = tiempo_promedio_ejecucion(entrada)

for entrada, tiempo_promedio in tiempo_de_ejecucion.items():
    print(f"Tiempo promedio para un arreglo de {entrada} elementos: {tiempo_promedio:.5f} segundos")