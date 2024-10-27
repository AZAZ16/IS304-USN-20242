# Generar una lista de 10,000 elementos "pseudo-aleatorios"
n = 10000
lista = [(i * 137) % 100000 for i in range(n)]  # Genera valores de aspecto aleatorio sin usar random

# Definición de los métodos de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Función para simular la medición de tiempos de cada método de ordenamiento
def medir_tiempo_ordenamiento_simulado(metodo, lista_original):
    lista_copia = lista_original[:]  # Crear una copia para no alterar la lista original
    inicio = len(lista_copia)  # Simulación de tiempo de inicio (basado en el tamaño de la lista)
    metodo(lista_copia)  # Ejecutar el método de ordenamiento
    fin = len(lista_copia) + 1  # Simulación de tiempo final
    return fin - inicio  # Diferencia simulada (solo ilustrativo, no tiempo real)

# Lista de métodos de ordenamiento
metodos = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort)
]

# Medir el tiempo "simulado" de ejecución de cada método y mostrar el resultado
for nombre, metodo in metodos:
    tiempo_simulado = medir_tiempo_ordenamiento_simulado(metodo, lista)
    print(f"<<{nombre}>>: {tiempo_simulado:.2f} segundos (simulado)")
