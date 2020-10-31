#!C:\Users\groso\AppData\Local\Programs\Python\Python37-32\python.exe
# -*- coding: utf-8 -*-

print("Content-type: text/html; charset=UTF-8")
print("")  

import save_db
import datetime
import cgi, os
import cgitb; cgitb.enable()

db = save_db.AnimalitosDb("root", "")
domicilios = db.get_all("domicilio")

# Field para obtener en que valor de la tabla se encuentra actualmente
datos = cgi.FieldStorage()

# Se obtiene el parametro id que representa el valor actual de la tabla
iden = int(datos["id"].value)

# Cantidad de botones para moverse en la tabla
cantidad_botones= (len(domicilios)-1)//5

html = f'''

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Animalitos</title>

    <link rel="stylesheet" href="/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/css/principal.css"/>
    <link rel="icon" type="image/jpeg" href="img/simon.jpeg">
    <script src="/js/principal.js"></script>

    <script>

        update_page({iden}, {cantidad_botones})
    
    </script>

</head>
<body class="main">

    <div class="principal-container mx-auto">

        <header class="principal-header text-center">
            <h1 class="titulo">Animalitos</h1>
            <p class="subtitulo">La mejor pagina para buscar mascotas</p>
        </header>
        <section class="t-section">
            <div class="nav-div">
                <nav class="nav-bar">
                    <a href="principal.py" class="nav-ref"><span class="nav-item"></span>Principal</a>
                    <a href="formulario.py" class="nav-ref"><span class="nav-item"></span>Informar mascotas</a>
                    <a href="tabla.py?id=0" class="nav-ref"><span class="nav-item"></span>Ver listado de mascotas</a>
                    <a href="estadisticas.py" class="nav-ref"><span class="nav-item"></span>Estadisticas</a>
                </nav>
            </div>
            <div class="container-content" style="overflow-x:auto;">

                <table id="myTable">
                    <tr>
                        <th onclick="sortTable(0)">Fecha Ingreso</th>
                        <th onclick="sortTable(1)">Comuna</th>
                        <th onclick="sortTable(2)">Nombre Calle</th>
                        <th onclick="sortTable(3)">Nombre contacto</th>
                        <th onclick="sortTable(4)">Total Mascotas</th>
                        <th onclick="sortTable(5)">Total fotos</th>
                    </tr>
                    '''
print(html)
domicilio_actual = 0

# Por cada domicilio entre los actuales
for domicilio in domicilios[iden*5:(iden*5)+5]:

    # Solo 5 domicilios
    if domicilio_actual == 5:
        break

    # Comuna del domicilio a informar
    comuna = db.comuna_by_id(domicilio[2])

    # Cantidad de mascotas en el domicilio a informar
    suma_mascota = db.count_all_mascotas(domicilio[0])

    # Todas las mascotas del domicilio
    mascotas_domicilio = db.mascota_from_domicilio(domicilio[0])

    # Contador de fotos
    cantidad_fotos = 0

    # Por cada mascota, contaremos cuantas fotos
    for mascota in mascotas_domicilio:
        cantidad_fotos += db.count_fotos_mascota(mascota[0])

    tabla = f'''

                    <tr onclick="hrefTable('#popup{domicilio_actual}')">
                        <td>{domicilio[1]}</td>
                        <td>{comuna}</td>
                        <td>{domicilio[3]}</td>
                        <td>{domicilio[6]}</td>
                        <td>{suma_mascota}</td>
                        <td>{cantidad_fotos}</td>
                    </tr>
            '''
    print(tabla)
    domicilio_actual += 1
print('''
                </table>
                <br>
                <div class= "button-nav">
                    <button onclick="previous_page();" class="button-ref">Anterior</button>
                ''')
for i in range(cantidad_botones+1):
    print(f'''
                    <a onclick = "update_page({i}, {cantidad_botones})" href=tabla.py?id={i} class="button-ref">{i+1}</a>
            ''')

print('''
                    <button onclick="next_page();" class="button-ref">Proxima</button>
                </div>
            </div>
        </section>
    </div>
    ''')


domicilio_actual = 0

total_fotos = 0
total_fotos2 = 0
for domicilio in domicilios[iden*5:(iden*5)+5]:
    
    region = db.region_by_comunaid(domicilio[2])
    comuna = db.comuna_by_id(domicilio[2])
    mascotas = db.mascota_from_domicilio(domicilio[0])
    tipo_mascota = db.mascota_by_id(mascotas[0][1])
    imagenes_mascota = db.image_from_domicilio(domicilio[0], 3)

    popup = f'''
            <div id="popup{domicilio_actual}" class="overlay">
                <div class="popupBody">
                    <h2 class="tittle">Información de un censo</h2>
                    <a class="cerrar" href="#">&times;</a>
                    <div class="popupContent">
                        <p class="font-censo">Región: <span>{region}</span></p>
                        <p class="font-censo">Comuna: <span>{comuna}</span></p>
                        <p class="font-censo">Calle: <span>{domicilio[3]}</span></p>
                        <p class="font-censo">N°Calle: <span>{domicilio[4]}</span></p>
                        <p class="font-censo">Sector: <span>{domicilio[5]}</span></p>
                        <hr class="censo">
                        <p class="font-censo">Nombre: <span>{domicilio[6]}</span></p>
                        <p class="font-censo">Email: <span>{domicilio[7]}</span></p>
                        <p class="font-censo">N°Celular: <span>{domicilio[8]}</span></p>
                        <hr class="censo">
                        <p class="font-censo">Tipo: <span>{tipo_mascota}</span></p>
                        <p class="font-censo">Edad: <span>{mascotas[0][2]}</span></p>
                        <p class="font-censo">Color: <span>{mascotas[0][3]}</span></p>
                        <p class="font-censo">Raza: <span>{mascotas[0][4]}</span></p>
                        <p class="font-censo">Esterilizado: <span>{db.esterilizado(mascotas[0][5])}</span></p>
                        <p class="font-censo">Vacunas al día: <span>{db.esterilizado(mascotas[0][6])}</span></p>
    '''

    print(popup)
    
    for i in range(len(imagenes_mascota)):

        
        name_image = os.path.splitext(imagenes_mascota[i][0])
        
        image_html = f'''
                        <div class="div-censo{i+1}">
                            <img class="imagen-censo{i+1}" src=/{name_image[0] + "image320" + name_image[1]} alt="Mascota" id = "mascota1" onclick="showImage('span-mascota{total_fotos}')"><br>
                        </div>
                        
        '''
        print(image_html)
        total_fotos += 1


    for i in range(len(imagenes_mascota)):

        name_image = os.path.splitext(imagenes_mascota[i][0])

        popup_image = f'''

                        <div class="span-div">
                            <span class="img800" id="span-mascota{total_fotos2}">
                                <img src=/{name_image[0] + "image800" + name_image[1]} class="imagen-ampliada" alt="Mascota">
                                <a class="cerrar" onclick="hideImage('span-mascota{total_fotos2}')">&times;</a>
                            </span>
                        </div>

        '''
        print(popup_image)
        total_fotos2+=1
    print('''
                    </div>
                </div>
            </div>
    ''')
    domicilio_actual+=1
    
print('''
</body>
</html>


''')

