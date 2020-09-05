entrada1 = '_servidor2'
entrada2 = '3servidor'

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def AFD(entrada):
    estado = 0

    for i in entrada:
        if estado == 0:
            if i == '_':
                estado = 1
            elif i in abc:
                estado = 2
            else:
                print(entrada +' ---> Error de entrada en estado 0')
                break

        elif estado == 1:
            if i == '_':
                estado = 1
            elif i in abc:
                estado = 3
            else:
                print(entrada +' ---> Error de entrada en estado 1')
                break

        elif estado == 2:
            if i in abc:
                estado = 2
            elif i in Num:
                estado = 4
                if entrada[-1] == i:
                    print(entrada + ' ---> Cumple la entrada')
            else:
                print(entrada + ' ---> Error de entrada en estado 2')
                break

        elif estado == 3:
            if i in abc:
                estado = 3
            elif i in Num:
                estado = 4
                if entrada[-1] == i:
                    print(entrada + ' ---> Cumple la entrada')
            else:
                print(entrada +' ---> Error de entrada en estado 3')
                break

        elif estado == 4:
            if i == '_':
                estado = 1
            elif i in abc:
                estado = 2
            elif i in Num:
                print(entrada + ' ---> Error de entrada')


AFD(entrada1)
AFD(entrada2)