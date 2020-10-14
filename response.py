#!C:\Users\groso\AppData\Local\Programs\Python\Python37-32\python.exe

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

# Tamaño maximo del archivo
MAX_FILE_SIZE = 1000000

# Mensaje de proceso
mensaje = "El archivo fue recibido correctamente"

# Tamaño del archivo ingresado
size = 0
tipo_real = ""

# Id de la comuna
id_comuna = db.get_comuna_id(form["comuna"].value)

# Data sobre el domicilio
data_domicilio = (

    datetime.datetime.now(), id_comuna, \
        form["calle"].value, form["numero"].value, \
            form["sector"].value, form["nombre"].value, form["email"].value, \
                form["celular"].value
)

# Mascota revisando actual
actual_mascota = 0

# Si el formulario tiene informacion
if len(form) > 0:

    fotos_array = []

    # Por cada mascota, revisaremos sus fotos
    while mensaje == "El archivo fue recibido correctamente":

        # String que indica en que mascota estoy
        string_mascota = 'foto-mascota' + str(actual_mascota)

        # Si no esta en el formulario, dejo de revisar fotos
        if string_mascota not in form:
            break

        # El arreglo de fotos de mascotas
        item = form[string_mascota]

        # Si son mas de una, es una lista, si no un valor
        if type(item) == list:
            quantity_item = len(item)
        else:
            quantity_item = 1

        # Por cada foto de las mascotas
        for i in range(quantity_item):

            if type(item) != list:
                fileitem = item
            else:
                fileitem = item[i]

            # El item no es vacio
            if fileitem.filename:

                try:

                    # Tomo el tamaño y tipo del archivo
                    size = os.fstat(fileitem.file.fileno()).st_size
                    tipo_real = filetype.guess(fileitem.file)

                    # Si el tipo es una imagen
                    if tipo_real != None and "image" in tipo_real.mime:

                        # Si el file es menor al tamaño maximo
                        if size <= MAX_FILE_SIZE:

                            fn = os.path.basename(fileitem.filename)
                            with open('./tmp/'+fn, 'wb') as f:
                                f.write(fileitem.file.read())
                            mensaje = "El archivo fue recibido correctamente"
                            data_foto = (

                            './tmp/'+fn, fn
                            )
                            fotos_array.append(data_foto)
                            actual_mascota+=1
                        else:

                            mensaje = "El archivo pesa mucho"
                            break
                    else:
                        mensaje = "Archivo no soportado"
                        break
                except IOError as e:
                    mensaje = "Error"
                    break
            else:

                mensaje = "No se recibio el archivo"
                break
        

    # Los archivos fueron procesados exitosamente
    if mensaje == "El archivo fue recibido correctamente":

        # Se guarda el domicilio en la db
        db.save_domicilio(data_domicilio)

        for i in range(actual_mascota):
        
            # Arreglo, si son mas de una es una lista, si no un valor
            if type(form["tipo-mascota"]) == list:
                

                data_mascota = (

                    int(form["tipo-mascota"][i].value), \
                        int(form["edad-mascota"][i].value), form["color-mascota"][i].value, \
                            form["raza-mascota"][i].value, int(form["esterilizado-mascota"][i].value), \
                                int(form["vacunas-mascota"][i].value), db.get_domicilio_id(form["calle"].value, form["sector"].value, form["nombre"].value)
                )
                db.save_mascota_domicilio(data_mascota)

                id_mascota = db.get_mascota_id(form["tipo-mascota"][i].value, form["edad-mascota"][i].value, \
                    form["color-mascota"][i].value, db.get_domicilio_id(form["calle"].value, \
                        form["sector"].value, form["nombre"].value), form["raza-mascota"][i].value)

            else:

                # El usuario ingresara una nueva mascota
                if form["tipo-mascota"].value == "9":
                    
                    # Si no se encuentra en la base de datos, la incluyo
                    if db.id_mascota_by_name(form["otro-mascota"].value) == []:
                        db.save_new_mascota(form["otro-mascota"].value)
                    
                    # El tipo de mascota sera el del input otro-mascota
                    tipo_mascota = db.id_mascota_by_name(form["otro-mascota"].value)[0][0]

                # Es una mascota que esta en la base de datos
                else:
                    tipo_mascota = form["tipo-mascota"].value

                # Datos para incluir a una mas
                data_mascota = (

                    int(tipo_mascota), \
                        int(form["edad-mascota"].value), form["color-mascota"].value, form["raza-mascota"].value, \
                            int(form["esterilizado-mascota"].value), int(form["vacunas-mascota"].value), \
                                db.get_domicilio_id(form["calle"].value, form["sector"].value, form["nombre"].value)
                )
                db.save_mascota_domicilio(data_mascota)

                # El id de la nueva mascota
                id_mascota = db.get_mascota_id(tipo_mascota, form["edad-mascota"].value, form["color-mascota"].value, \
                    db.get_domicilio_id(form["calle"].value, form["sector"].value, form["nombre"].value), form["raza-mascota"].value)

            # Guardo las fotos en la base de datos
            db.save_foto_mascota((fotos_array[i][0], fotos_array[i][1], id_mascota))
        
    # Las fotos tuvieron error al subirse, las borro de la carpeta tmp
    else:

        for i in range(len(fotos_array)):

            os.remove(fotos_array[0][0])



html=f'''

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Animalitos</title>

    <link rel="stylesheet" href="css/bootstrap.min.css" />
    <link rel="stylesheet" href="css/principal.css"/>
    <link rel="icon" type="image/jpeg" href="img/simon.jpeg">
    <script src="js/principal.js"></script>
    <script src="js/validador.js"></script>

</head>
<body class="main">
            <div class="container-content">
                <h2>{mensaje}</h2>
                <a href = "principal.py"><button class="button-sub" type="button" id="button-home" ">Volver al Inicio</button></a>                
            </div>
</body>
</html>

'''

print(html)

