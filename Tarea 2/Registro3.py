import csv

with open('Registro3.csv') as File:
    reader = csv.reader(File, delimiter=";")

    aux = reader

    for info in aux:
       print("REGISTRO: {0}, TIPO: {1}, RAZA: {2}, COLOR: {3}, TAMAÑO: {4}".format(info[0], info[1], info[2], info[3], info[4]))
       print(input("Click Enter"))
<<<<<<< HEAD

print(type(aux))
print(input("Click Enter para Finalizar"))
=======
        
print(type(aux))
print(input("Click Enter para Finalizar"))
>>>>>>> 863955fb77ca1baf3b338acdfe6bd8eea965fa04
