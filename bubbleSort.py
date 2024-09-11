import time
#tamanos = [200000, 500000, 1000000] # Cantidad de elementos base por archivo
tamanos = [100000] # Cantidad de elementos base por archivo

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

    def bubbleSort(arr):
        n = len(arr)  # Se obtiene el tamaño del arreglo.

        # Se ejecuta un bucle para cada elemento del arreglo.
        for i in range(n):
            swapped = False  # Bandera que indica si se han intercambiado elementos.

            # El bucle interno recorre el arreglo desde el primer hasta el penúltimo elemento no ordenado.
            for j in range(0, n-i-1):
                # Si el elemento actual es mayor que el siguiente, se intercambian.
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]  # Se realiza el intercambio.
                    swapped = True  # Se cambia la bandera, indicando que hubo un intercambio.

            # Si no hubo intercambios en la pasada, el arreglo ya está ordenado, y se termina el proceso.
            if not swapped:
                break  # Se sale del bucle externo si no se hizo ningún intercambio.

    # Código extraido de: https://www.geeksforgeeks.org/bubble-sort-algorithm/

    hora_inicio = time.strftime("%H:%M:%S")
    start_time = time.time()

    bubbleSort(my_array)

    end_time = time.time()
    hora_final = time.strftime("%H:%M:%S")
    execution_time = end_time - start_time

    archivo = open("Tarea 1\\tiempos.txt", "a")

    archivo.write(str("BubbleSort con {}_{}\n").format(dataset[tipo],execution))
    archivo.write("Hora de inicio: {}\n".format(hora_inicio))
    archivo.write("Hora de finalización: {}\n".format(hora_final))
    archivo.write("Tiempo transcurrido: {}\n".format(execution_time))
    archivo.write(">----------------------------------<\n")

    archivo.close()
