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

    <link rel="stylesheet" href="/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/css/principal.css" />
    <link rel="icon" type="image/jpeg" href="img/foton.png">
    <link rel="script" href="/js/principal.js">

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
            <div class="container-content">
                <figure>
                    <img src="/img/img.jpeg" alt="Image" class="img-fluid principal-imagen center-image">
                </figure>

                <div class="info-div">
                    <h2 class="tittle">Bienvenidos a Animalitos</h2>
                    <p style="line-height: 110%; text-align: center">Animalitos es la primera pagina web encargada de realizar
                        un censo a las mascotas del país <br>
                        contamos con una gran cantidad de datos
                        de las distintas mascotas de todos los chilenos, <br> no te quedes fuera de esta
                        gran iniciativa</p>
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

            <img class="imagen-mascota" src="/{source_foto}" alt="Mascota">
            <a class="font-mascotas">Comuna: </a><a class="font-informado"> {str(db.comuna_by_id(p[2]))}</a><br>
            <a class="font-mascotas">Calle: </a><a class="font-informado"> {str(p[3])}</a><br>
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
        </section>
    </div>
</body></html>
'''
print(html2)