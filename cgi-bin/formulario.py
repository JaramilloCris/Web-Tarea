#!C:\Users\groso\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

print("Content-type: text/html; charset=UTF-8")
print("")  

import cgi, os
import cgitb; cgitb.enable()
import save_db as sd
import datetime
import filetype

# Saco el formulario y acceso a la base de datos
form = cgi.FieldStorage()
db = sd.AnimalitosDb("root", "")

# Estado de formulario
state_formulario = 'visible'
state_result = 'hidden'

# Tamaño maximo del archivo
MAX_FILE_SIZE = 1000000

# Mensaje de proceso
mensaje = "Hemos recibido su información, muchas gracias por colaborar"
popup = '#'

# Tamaño del archivo ingresado
size = 0
tipo_real = ""

# Mascota revisando actual
actual_mascota = 0

# Si el formulario tiene informacion
if len(form) > 0:

    popup = '#popup-validado'
    state_formulario = 'hidden'
    state_result = 'visible'

    # Id de la comuna
    id_comuna = db.get_comuna_id(form["comuna"].value)

    # Data sobre el domicilio
    data_domicilio = (

        datetime.datetime.now(), id_comuna, \
            form["calle"].value, form["numero"].value, \
                form["sector"].value, form["nombre"].value, form["email"].value, \
                    form["celular"].value
    )

    fotos_array = []

    # Por cada mascota, revisaremos sus fotos
    while mensaje == "Hemos recibido su información, muchas gracias por colaborar":

        # String que indica en que mascota estoy
        string_mascota = 'foto-mascota' + str(actual_mascota)

        # Si no esta en el formulario, dejo de revisar fotos
        if string_mascota not in form:
            break

        # El arreglo de fotos de mascotas
        item = form[string_mascota]

        # Si son mas de una, es una lista, si no un valor
        quantity_item = len(item) if type(item) == list else 1

        fotos_actual_mascota = []
        # Por cada foto de las mascotas
        for i in range(quantity_item):

            # Las fotos de las mascotas (cuidado con el trabajo con listas)
            fileitem = item if type(item) != list else item[i]

            # El item no es vacio
            if fileitem.filename:

                try:

                    # Tomo el tamaño y tipo del archivo
                    size = os.fstat(fileitem.file.fileno()).st_size
                    # Si el file es menor al tamaño maximo
                    if size <= MAX_FILE_SIZE:

                        fn = os.path.basename(fileitem.filename)
                        f = open("tmp/" + fn, 'wb')
                        file_d = fileitem.file.read()
                        f.write(file_d)
                        f.close()
                        mensaje = "Hemos recibido su información, muchas gracias por colaborar"
                        data_foto = (

                        "tmp/" + fn, fn
                        )
                        fotos_actual_mascota.append(data_foto)
                        tipo_real = filetype.guess("./tmp/" + fn)
                        if tipo_real == None or "image" not in tipo_real.mime:

                            mensaje = "Archivo no soportado"
                            break

                    else:

                        mensaje = "El archivo pesa mucho"
                        break
             
                except IOError as e:
                    mensaje = "Error"
                    break
            else:

                mensaje = "No se recibio el archivo"
                break
        fotos_array.append(fotos_actual_mascota)
        actual_mascota+=1
        

    # Los archivos fueron procesados exitosamente
    if mensaje == "Hemos recibido su información, muchas gracias por colaborar":


        # Se guarda el domicilio en la db
        id_domicilio = db.save_domicilio(data_domicilio)

        for i in range(actual_mascota):

            # Valores
            tipo_mascota = int(form["tipo-mascota"][i].value) if type(form["tipo-mascota"]) == list else int(form["tipo-mascota"].value)
            edad_mascota = int(form["edad-mascota"][i].value) if type(form["edad-mascota"]) == list else int(form["edad-mascota"].value)
            color_mascota = form["color-mascota"][i].value if type(form["color-mascota"]) == list else form["color-mascota"].value
            raza_mascota = form["raza-mascota"][i].value if type(form["raza-mascota"]) == list else form["raza-mascota"].value
            esterilizado_mascota = int(form["esterilizado-mascota"][i].value) if type(form["esterilizado-mascota"]) == list else int(form["esterilizado-mascota"].value)
            vacunas_mascota = int(form["vacunas-mascota"][i].value) if type(form["vacunas-mascota"]) == list else int(form["vacunas-mascota"].value)
            otro_mascota = form["otro-mascota"][i].value if type(form["otro-mascota"]) == list else form["otro-mascota"].value
        
            # El usuario ingresara una nueva mascota
            if tipo_mascota == 9:
                
                # Si no se encuentra en la base de datos, la incluyo
                if db.id_mascota_by_name(otro_mascota) == []:
                    db.save_new_mascota(otro_mascota)
                
                # El tipo de mascota sera el del input otro-mascota
                tipo_mascota = db.id_mascota_by_name(otro_mascota)[0][0]

            data_mascota = (tipo_mascota, edad_mascota, color_mascota, raza_mascota, esterilizado_mascota, vacunas_mascota, id_domicilio)
            id_mascota = db.save_mascota_domicilio(data_mascota)

            # Guardo las fotos en la base de datos
            for j in range(len(fotos_array[i])):
                db.save_foto_mascota((fotos_array[i][j][0], fotos_array[i][j][1], id_mascota))
        
    # Las fotos tuvieron error al subirse, las borro de la carpeta tmp
    else:
        for mascota_fotos in fotos_array:
            for foto in mascota_fotos:
                os.remove(foto[0])


html = f'''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
    <meta content="utf-8" http-equiv="encoding">
    <title>Animalitos</title>

    <link rel="stylesheet" href="/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/css/principal.css"/>
    <link rel="icon" type="image/jpeg" href="img/simon.jpeg">
    <script src="/js/principal.js"></script>
    <script src="/js/validador.js"></script>

</head>
<body class="main">

    <div class="principal-container mx-auto">

        <header class="principal-header text-center">
            <h1 class="titulo">Formulario de mascotas</h1>
            <p class="subtitulo">La mejor pagina para buscar mascotas</p>
        </header>
        <section id="principal-section" class="t-section">
            <div class="nav-div">
                <nav class="nav-bar">
                    <a href="principal.py" class="nav-ref"><span class="nav-item"></span>Principal</a>
                    <a href="formulario.py" class="nav-ref"><span class="nav-item"></span>Informar mascotas</a>
                    <a href="tabla.py?id=0" class="nav-ref"><span class="nav-item"></span>Ver listado de mascotas</a>
                    <a href="estadisticas.py" class="nav-ref"><span class="nav-item"></span>Estadisticas</a>
                </nav>
            </div>
            <div class="container-content" style="visibility: {state_result}; position: absolute; width: 100%;">
                <h4 class="tittle">{mensaje}</h4>
                    <div class="popupContent">
                        <div class="form-botones">
                            <button class="ver-button" onclick="hrefTable('principal.py')">Volver al inicio</button>
                        </div>
                    </div>
            </div>

            <div id="principal-div">
                <form style="visibility: {state_formulario}" id="form1" enctype="multipart/form-data" method="POST" action="formulario.py" onsubmit="return validarFormulario()">
                    <div class="container-content">
                        <h2 style="font-weight: bold">Domicilio:</h2>
                        <br>
                        <div class="input-div">
                            <select class="select-custom" id="region" name="region" onchange="buscar_ciudad()" required="required">
                                <option value="" selected="selected">Regiones</option>
                                <option value="1">Metropolitana de Santiago</option>
                                <option value="2">Arica y Parinacota</option>
                                <option value="3">Tarapacá</option>
                                <option value="4">Antofagasta</option>
                                <option value="5">Atacama</option>
                                <option value="6">Coquimbo</option>
                                <option value="7">Valparaiso</option>
                                <option value="8">Libertador Gral. Bernardo O Higgins</option>
                                <option value="9">Maule</option>
                                <option value="10">Ñuble</option>
                                <option value="11">Biobío</option>
                                <option value="12">La Araucanía</option>
                                <option value="13">Los Ríos</option>
                                <option value="14">Los Lagos</option>
                                <option value="15">Aisén del Gral. Carlos Ibáñez del Campo</option>
                                <option value="15">Magallanes y de la Antártica Chilena</option>
                            </select>
                            <select class="select-custom" name="comuna" id="comuna">
                                <option value="0">Comunas por Region</option>
                            </select>
                        </div>
                        <div class="input-div">
                            <input class="input-style" name="calle" id="id-calle" size="100" maxlength="250" placeholder="Nombre Calle..." required="required">
                        </div>

                        <div class="input-div">
                            <input class="input-style" name="numero" id="id-numero" size="20" required="required" maxlength="20" placeholder="Número de domicilio...">
                        </div>
                        <div class="input-div">
                            <input class="input-style" name="sector" id="id-sector" size="100"  maxlength="100" placeholder="Sector...">

                        </div>
                    </div>
                    <div class="container-content">
                        <h2 style="font-weight: bold">Datos de contacto: </h2>
                        <br>
                        <div class="input-div">
                            <input class="input-style" placeholder="Nombre..." name="nombre" id="id-nombre" size="100" maxlength="200" required="required">
                        </div>
                        <div class="input-div">
                            <input class="input-style" placeholder="Email..." name="email" id="id-email" size="100" type="email" required="required">
                        </div>
                        <div class="input-div">
                            <input class="input-style" placeholder="Número de Celular..." name="celular" id="id-celular" size="15" type="tel">
                            <small class="form-text text-muted">Ejemplo: +56912345678</small>
                        </div>
                    </div>
                    <div id="div-mascota" class="container-content">
                        <h2 style="font-weight: bold">Información de mascota: </h2>
                        <div class="input-div">
                            <br>
                            <select id="raza0" class="select-custom" name="tipo-mascota" onchange="hideInput('raza0','text-value0')" required="required">
                                <option value="">Seleccione un tipo</option>
                                <option value="1">Perro</option>
                                <option value="2">Gato</option>
                                <option value="3">Pez</option>
                                <option value="4">Tortuga</option>
                                <option value="5">Hámster</option>
                                <option value="6">Loro</option>
                                <option value="7">Iguana</option>
                                <option value="8">Araña</option>
                                <option value="9">Otro</option>
                            </select>
                            <input hidden id="text-value0" name="otro-mascota" class="input-style" size="40" maxlength="40" placeholder="Otro...">
                        </div>
                        <div class="input-div">
                            <input name="edad-mascota" class="input-style" id="id-annos0" placeholder="Edad en años..." required="required">
                        </div>
                        <div class="input-div">
                            <input name="color-mascota" placeholder="Color..." class="input-style" id="id-color0" size="30"  maxlength="30" required="required">
                        </div>
                        <div class="input-div">
                            <input name="raza-mascota" placeholder="Raza..." class="input-style" id="id-raza0" size="30" maxlength="30" required="required">
                        </div>
                        <div class="input-div">
                            <label for="id-esterilizado0">Esterilizado:</label>
                            <br>
                            <select id="id-esterilizado0" class="input-style" name="esterilizado-mascota" required="required">
                                <option value="">Seleccione opción</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                                <option value="2">No aplica</option>
                            </select>
                        </div>
                        <div>
                            <label for="id-vacunado0">Vacunas al día:</label>
                            <br>
                            <select id="id-vacunado0" name="vacunas-mascota" class="input-style" required="required">
                                <option value="">Seleccione opción</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                                <option value="2">No aplica</option>
                            </select>
                        </div>
                        <div>
                            <label for="id-foto0-0">Foto:</label>

                            <br>
                            <input name="foto-mascota0" id="id-foto0-0" size="15" type="file" required>

                            <button class="button-sub" type="button" id="addFile0" onclick="addInputFile(4, 'container-file0', 0)">Añadir archivos</button>
                        </div>
                        <div id="container-file0">
                        </div>
                        <br>
                    </div>
                </form>
                <div id="botones-form" class="form-botones">
                    <button class="button-sub-out" id="clone-mascota" type="button" onclick="clonar('div-mascota')" >Informar otra mascota en este domicilio</button>
                    <button class="button-sub-out" id="subm" onclick="hrefTable('#popup-verificacion')" >Enviar</button>
                </div>
                <div id="popup-verificacion" class="overlay-ver">
                    <div class="popupBody-ver">
                        <h4 class="tittle">¿Está seguro que desea enviar esta información?</h4>
                        <a class="cerrar" href="#">&times;</a>
                        <div class="ver-botones">
                            <button class="ver-button" type="submit" form="form1" onclick="validarFormulario()">Sí, estoy total y absolutamente seguro</button>
                            <button class="ver-button" onclick="hrefTable('#')">No estoy seguro, quiero volver al formulario</button>
                        </div>
                    </div>
                </div>
                <div id="popup-validado" class="overlay-ver">
                    <div class="popupBody-ver">
                        <h4 class="tittle">{mensaje}</h4>
                        <div class="popupContent">
                            <div class="form-botones">
                                <button class="ver-button" onclick="hrefTable('principal.html')">Volver al inicio</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="popup-error" class="overlay-ver">
                    <div class="popup-error">
                        <h4 class="tittle" id="mensaje-error">Error</h4>
                        <h4 class="tittle" id="mensaje-error1"></h4>
                        <a class="cerrar" href="#">&times;</a>
                    </div>
                </div>
            </div>
        </section>
    </div>
</body>
    <script>

        hrefTable({popup});
    
    </script>
</html>
'''
print(html)