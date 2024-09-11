import time
tamanos = [200000, 500000, 1000000] # Cantidad de elementos base por archivo
dataset = ["ordered_dataset", "partially_ordered_dataset", "random_dataset"]
directorio = ["Tarea 1\\ordered_datasets\\ordered_dataset", "Tarea 1\\partially_ordered_datasets\\partially_ordered_dataset", "Tarea 1\\random_datasets\\random_dataset"]
tipo = int(input("Ingrese el tipo de dataset a ordenar\n (0: Ordenado, 1: Parcialmente Ordenado, 2: Aleatorio): "))
for execution in tamanos:

    archivo = open(str("{}_{}.txt".format(directorio[tipo],execution)), "r")
    for linea in archivo:
        my_array = linea
    my_array = linea[1:-1]
    my_array = [int(x) for x in my_array.split(",")]

    archivo.close()

    def median_of_three(array, low, high):
        # Se calcula el índice del medio del array entre los límites low y high.
        mid = (low + high - 1) // 2

        # Se evalúan las relaciones entre los valores en los índices low, mid y high-1 
        # para determinar cuál de estos es el valor mediano. 
        # Se devuelven diferentes valores según las comparaciones.

        if array[low] <= array[mid] <= array[high-1]:
            return array[mid]
        if array[high-1] <= array[mid] <= array[low]:
            return array[mid]
        if array[low] <= array[high-1] <= array[mid]:
            return array[high-1]
        if array[mid] <= array[high-1] <= array[low]:
            return array[high-1]
        return array[low]


    def partition(array, low, high):
        # Selecciona el pivote usando la función median_of_three.
        pivot = median_of_three(array, low, high)
        i = low - 1   # Inicializa el índice 'i' un paso antes del límite 'low'.

        # Recorre el subarray desde el índice 'low' hasta 'high'.
        for j in range(low, high):
            # Si el elemento actual es menor o igual al pivote, intercambia 
            # el elemento con el que está en la posición 'i+1'.
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        # Coloca el pivote en su posición correcta, intercambiando el elemento en 'i+1' con el último.
        array[i+1], array[high] = array[high], array[i+1]
        return i+1  # Devuelve el índice del pivote.

    def quicksort(array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = partition(array, low, high)  # Se obtiene el índice del pivote después de particionar el array.
            
            # Llamadas recursivas para ordenar las dos mitades del array
            # (izquierda y derecha del pivote).
            
            quicksort(array, low, pivot_index-1)
            quicksort(array, pivot_index+1, high)

    hora_inicio = time.strftime("%H:%M:%S")
    start_time = time.time()

    quicksort(my_array)

    end_time = time.time()
    hora_final = time.strftime("%H:%M:%S")
    execution_time = end_time - start_time

    archivo = open("Tarea 1\\tiempos.txt", "a")

    archivo.write(str("QuickSort con {}_{}\n").format(dataset[tipo],execution))
    archivo.write("Hora de inicio: {}\n".format(hora_inicio))
    archivo.write("Hora de finalización: {}\n".format(hora_final))
    archivo.write("Tiempo transcurrido: {}\n".format(execution_time))
    archivo.write(">----------------------------------<\n")

    archivo.close()
