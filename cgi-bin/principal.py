#!C:\Users\groso\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

print("Content-type: text/html; charset=UTF-8")
print("")   

import save_db

db = save_db.AnimalitosDb("root", "")
last_domicilio = db.ultimo_domicilio(5)

html = f'''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Animalitos</title>

    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>

    <link rel="stylesheet" href="/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/css/principal.css" />

    <link rel="icon" type="image/jpeg" href="img/foton.png">
    <link rel="script" href="/js/principal.js">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    

</head>

<body class="main">

    <div class="principal-container mx-auto">

        <header class="principal-header text-center">
            <h1 class="titulo">Animalitos</h1>
            <p class="subtitulo">La mejor pagina para buscar mascotas</p>
        </header>
        <div class="t-section">
            <div class="nav-div">
                <nav class="nav-bar">
                    <a href="principal.py" class="nav-ref"><span class="nav-item"></span>Principal</a>
                    <a href="formulario.py" class="nav-ref"><span class="nav-item"></span>Informar mascotas</a>
                    <a href="tabla.py?id=0" class="nav-ref"><span class="nav-item"></span>Ver listado de mascotas</a>
                    <a href="estadisticas.py" class="nav-ref"><span class="nav-item"></span>Estadisticas</a>
                </nav>
            </div>
            <div class="container-content">
                <figure>
                    <img src="/img/img.jpeg" alt="Image" class="img-fluid principal-imagen center-image">
                </figure>

                <div class="info-div">
                    <h2 class="tittle">Bienvenidos a Animalitos</h2>
                    <p style="line-height: 110%; text-align: center">Animalitos es la primera pagina web encargada de realizar
                        un censo a las mascotas del país <br></p>
                </div>
                <h2>Mapa de censos</h2>
                <hr class="new">
                <div style = "position: relative; left: 15%">
                    <div id="mapid" style="width: 70%; height: 400px; margin-bottom: 50px; display: inline-block;"></div>
                </div>
                
                <div class="container-me">

                    <h2>Últimas mascotas informadas</h2>
                    '''
print(html)
number_domicilio = 0
for p in last_domicilio:
    source_foto = db.image_from_domicilio(p[0],1)[0][0]
    number_domicilio+=1


    val = f'''<hr class="new">
        <div>
            <div class="div-photomain">
                <img class="imagen-mascota" src="/{source_foto}" alt="Mascota">
            </div>
            <div>
                <a class="font-mascotas">Comuna: </a><a class="font-informado"> {str(db.comuna_by_id(p[2]))}</a><br>
                <a class="font-mascotas">Calle: </a><a class="font-informado"> {str(p[3])}</a><br>
            </div>
        '''
    print(val)
    mascotas_domicilio = db.get_sum_mascotas(p[0])

    for l in mascotas_domicilio:
        mascota = db.mascota_by_id(l[0])

        val2 = f'''
            <a class="font-mascotas">{mascota}: </a> <a class="font-informado"> {l[1]}</a><br>
            '''

        print(val2)
    print("<br><br><br>")

html2 = '''
                </div><br>
                </div>
            </div>
        </div>
    </div>
</body>
<script type="text/javascript" src="/js/regiones.json"></script>
<script src="/js/map.js"></script>

</html>
'''
print(html2)