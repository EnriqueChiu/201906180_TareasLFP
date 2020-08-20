from xml.dom import minidom
documento = minidom.parse("Registro2.xml")



numero = int(0)
while 4>numero :

    registro = documento.getElementsByTagName("Dato")[numero]
    carnet = documento.getElementsByTagName("carnet")[numero]
    nombre = documento.getElementsByTagName("Nombre")[numero]
    dpi = documento.getElementsByTagName("DPI")[numero]
    carrera = documento.getElementsByTagName("Carrera")[numero]

    print( registro.firstChild.data)
    print("Carnet: %s"% carnet.firstChild.data)
    print("Nombre: %s"% nombre.firstChild.data)
    print("DPI: %s"% dpi.firstChild.data)
    print("Carrera: %s" %carrera.firstChild.data)
    print(input("Click Enter"))

    print()
    numero=numero +1
    
print(type(documento))
print(input("Click Enter para Finalizar"))
