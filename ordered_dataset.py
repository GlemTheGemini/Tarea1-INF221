tamanos = [200000, 500000, 1000000] # Cantidad de elementos base por archivo

for n in tamanos:
    print("Creando data set ordenado con {} elementos...".format(n))
    archivo = open(str("Tarea 1\\ordered_datasets\\ordered_dataset_{}.txt".format(n)), "w")

    to_write = "["
    numbers = list(range(1, (n+1)))

    for number in numbers:
        to_write += str(number) + ","

    to_write = to_write[:-1] + "]"
    archivo.write(to_write)
    print("- Archivo ordered_dataset.txt creado con {} elementos".format(n))

    archivo.close()
print("Archivos creados con éxito")