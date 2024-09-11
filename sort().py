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

    hora_inicio = time.strftime("%H:%M:%S")
    start_time = time.time()

    my_array.sort()

    end_time = time.time()
    hora_final = time.strftime("%H:%M:%S")
    execution_time = end_time - start_time

    archivo = open("Tarea 1\\tiempos.txt", "a")

    archivo.write(str("Sort() con {}_{}\n").format(dataset[tipo],execution))
    archivo.write("Hora de inicio: {}\n".format(hora_inicio))
    archivo.write("Hora de finalización: {}\n".format(hora_final))
    archivo.write("Tiempo transcurrido: {}\n".format(execution_time))
    archivo.write(">----------------------------------<\n")

    archivo.close()
