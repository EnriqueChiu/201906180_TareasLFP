import webbrowser

#Lista
nombre = ['Julio', 'David', 'Alex', 'Maria', 'Pedro', 'Naruto', 'Mirai', 'Yui', 'Oscar', 'Hina']
edad = [19, 22, 21, 20, 58, 30, 15, 16, 42, 17]
activo = ['Si', 'Si', 'No', 'No', 'No', 'Si', 'Si', 'Si', 'No', 'Si',]
saldo = [5000, 4500, 1200, 2500, 8062, 10000, 4444, 8, 1234, 777]


web = open('Tarea4.html', 'w')
x = 1
mensaje = """
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="utf-8" />
                <meta name="author" content="Julio Enrique Wu Chiu" />
                <title>TAREA 4</title>
            <style>
                body{background-image: url('fondo.jpg')}
                body{font-family: 'Comic Sans MS'; color:aliceblue; padding:80px}
                table{border-collapse:collapse}
                th {border: 4px crimson solid; margin:auto; color:yellow}
                td {border: 4px crimson solid; padding:10px; width:200px; margin:auto; text-align:center}
            </style>
            </head>
            <body>
            <center>
                <table class="registro">
                    <thead style="background-color:">
                        <tr>
                            <th colspan="5"><h1>REPORTE HTML </h1></th>
                        </tr>
                        <tr>
                            <td><h2>REGISTRO</h2></td>
                            <td><h2>NOMBRE</h2></td>
                            <td><h2>EDAD</h2></td>
                            <td><h2>ACTIVO</h2></td>
                            <td><h2>SALDO</h2></td>
                        </tr>
                    </thead>
                    <tbody>"""
web.write(mensaje)
n = 0
while n < 10:
                        a = nombre[n]
                        b = edad[n]
                        c = activo[n]
                        d = saldo[n]
                        arrayVer = [a, b, c, d]
                        texto = "<tr> <td>"+str(x)+"</td><td>"+str(a)+"</td><td>"+str(b)+"</td><td>"+str(c)+"</td><td>"+str(d)+"</td></tr>"
                        x += 1
                        n += 1
                        web.write(texto)
mensaje2 ="""
                    </tbody>
                </table>
            </center>
            </body>
            </html>
            """
web.write(mensaje2)
web.close()

webbrowser.open_new_tab('Tarea4.html')
