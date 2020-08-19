def menu():

    print("SELECIONAL ALGUNAS DE LAS OPCIONES")
    print("1) Registro 1 _ JSON")
    print("2) Registro 2 _ XML")
    print("3) Registro 3 _ CSV")
    print("4) Salir")

while True:
    menu()
    opciones = input("Ingrese un numero -->")

    if opciones == "1":
        print()
        import Registro1
        print()
    elif opciones == "2":
        print()
        import Registro2
        print("")
    elif opciones == "3":
        print()
        import Registro3
        print("")
    elif opciones == "4":
        break
    else:
        print()
        print("No ingreso un numero valido")
        print()
