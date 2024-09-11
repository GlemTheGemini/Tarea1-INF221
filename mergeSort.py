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

    def mergeSort(arr):
        # Caso base: Si el arreglo tiene un solo elemento o está vacío, ya está ordenado, así que se devuelve tal cual.
        if len(arr) <= 1:
            return arr

        # Se encuentra el punto medio del arreglo para dividirlo en dos mitades.
        mid = len(arr) // 2
        leftHalf = arr[:mid]  # Se toma la mitad izquierda del arreglo.
        rightHalf = arr[mid:]  # Se toma la mitad derecha del arreglo.

        # Se llama recursivamente a mergeSort para ordenar ambas mitades.
        sortedLeft = mergeSort(leftHalf)
        sortedRight = mergeSort(rightHalf)

        # Finalmente, se combinan las dos mitades ya ordenadas.
        return merge(sortedLeft, sortedRight)

    def merge(left, right):
        result = []  # Arreglo donde se almacenará el resultado final ya ordenado.
        i = j = 0  # Índices para recorrer las listas izquierda y derecha.

        # Mientras haya elementos en ambas mitades, se comparan y se añaden al resultado en orden.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])  # Si el elemento de la izquierda es menor, se agrega primero.
                i += 1  # Se incrementa el índice de la izquierda.
            else:
                result.append(right[j])  # Si el elemento de la derecha es menor, se agrega primero.
                j += 1  # Se incrementa el índice de la derecha.

        # Si quedan elementos en cualquiera de las dos mitades (porque una pudo tener más elementos),
        # se añaden al final del arreglo resultante.
        result.extend(left[i:])  # Se añaden los elementos restantes de la mitad izquierda.
        result.extend(right[j:])  # Se añaden los elementos restantes de la mitad derecha.

        # Se devuelve el arreglo completamente ordenado.
        return result

    # Código extraido de: https://www.w3schools.com/dsa/dsa_algo_quicksort.php

    hora_inicio = time.strftime("%H:%M:%S")
    start_time = time.time()

    mergeSort(my_array)

    end_time = time.time()
    hora_final = time.strftime("%H:%M:%S")
    execution_time = end_time - start_time

    archivo = open("Tarea 1\\tiempos.txt", "a")

    archivo.write(str("MergeSort con {}_{}\n").format(dataset[tipo],execution))
    archivo.write("Hora de inicio: {}\n".format(hora_inicio))
    archivo.write("Hora de finalización: {}\n".format(hora_final))
    archivo.write("Tiempo transcurrido: {}\n".format(execution_time))
    archivo.write(">----------------------------------<\n")

    archivo.close()
