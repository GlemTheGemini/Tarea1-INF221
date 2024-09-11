import random

tamanos = [200000, 500000, 1000000] # Cantidad de elementos base por archivo
cuantity = 10 # Cantidad de archivos a crear
print("Creando archivos...")
for i in tamanos:
    archivo = open(str("Tarea 1\\random_datasets\\random_dataset_{}.txt".format(i)), "w")
    
    to_write = "["

    random_numbers = list(range(1, i+1))
    random.shuffle(random_numbers)

    for number in random_numbers:
        to_write += str(number) + ","
    
    to_write = to_write[:-1] + "]"
    archivo.write(to_write)

    print("- Archivo random_dataset_{}.txt creado con {} elementos".format(i, i))
    archivo.close()
print("Archivos creados con éxito")