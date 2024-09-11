import random

tamanos = [200000, 500000, 1000000] # Cantidad de elementos base por archivo
percentage = 65 # Porcentaje de elementos ordenados

print("Creando archivos...")

for n in tamanos:
    archivo = open(str("Tarea 1\\partially_ordered_datasets\\partially_ordered_dataset_{}.txt".format(n)), "w")
    write = "["

    # Crear lista ordenada
    for j in range(1, int(n*percentage/100)+1):
        write += str(j) + ","

    # Crear lista desordenada
    random_numbers = list(range(1, int(n*((100-percentage)/100))+1))
    random.shuffle(random_numbers)
    for number in random_numbers:
        write += str(number + int(n*percentage/100)) + ","

    write = write[:-1] + "]"
    archivo.write(write)
    
    print("- Archivo partially_ordered_dataset_{}.txt creado con el {}%% de los elementos ordenados".format(n,percentage))
    archivo.close()

print("Archivos creados con éxito")