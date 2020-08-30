import json

archivo = './Registro1.json'
with open(archivo, 'r') as reader:
        for line in reader:
            print(line, input("Click Enter"))

print(type(archivo))
print(input("Click Enter para Finalizar"))