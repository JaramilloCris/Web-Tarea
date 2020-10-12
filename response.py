#!C:\Users\Tobal\AppData\Local\Programs\Python\Python37\python.exe

print("Content-type: text/html; charset=UTF-8")
print("")   

import cgi, os
import cgitb; cgitb.enable()
import save_db as sd
from datetime import date
import filetype

# Saco el formulario y acceso a la base de datos
form = cgi.FieldStorage()
db = sd.AnimalitosDb("root", "")

# Tamaño maximo del archivo
MAX_FILE_SIZE = 1000000

# Mensaje de proceso
mensaje = ""

# Tamaño del archivo ingresado
size = 0
tipo_real = ""

    # Id de la comuna
id_comuna = db.get_comuna_id(form["comuna"].value)

# Data sobre el domicilio
data_domicilio = (

    date.today(), id_comuna, \
        form["calle"].value, form["numero"].value, \
            form["sector"].value, form["nombre"].value, form["email"].value, \
                form["celular"].value
)

# Se guarda el domicilio en la db
db.save_domicilio(data_domicilio)

# Mascota revisando actual
actual_mascota = 0

# Si el formulario tiene informacion
if len(form) > 0:

    # Por cada mascota ingresada
    while True:
        
        # String que indica en que mascota estoy
        string_mascota = 'foto-mascota' + str(actual_mascota)

        # Si no esta en el formulario, dejo de ingresar mascotas
        if string_mascota not in form:
            break

        # Arreglo, si son mas de una es una lista, si no un valor
        if type(form["tipo-mascota"]) == list:
            
            data_mascota = (

                int(form["tipo-mascota"][actual_mascota].value), \
                    int(form["edad-mascota"][actual_mascota].value), form["color-mascota"][actual_mascota].value, \
                        form["raza-mascota"][actual_mascota].value, int(form["esterilizado-mascota"][actual_mascota].value), \
                             int(form["vacunas-mascota"][actual_mascota].value), db.get_domicilio_id(form["calle"].value, form["sector"].value, form["nombre"].value)
            )
            db.save_mascota_domicilio(data_mascota)

            id_mascota = db.get_mascota_id(form["tipo-mascota"][actual_mascota].value, form["edad-mascota"][actual_mascota].value, \
                 form["color-mascota"][actual_mascota].value, db.get_domicilio_id(form["calle"].value, \
                     form["sector"].value, form["nombre"].value), form["raza-mascota"][actual_mascota].value)

        else:

            data_mascota = (

                int(form["tipo-mascota"].value), \
                    int(form["edad-mascota"].value), form["color-mascota"].value, form["raza-mascota"].value, \
                        int(form["esterilizado-mascota"].value), int(form["vacunas-mascota"].value), \
                            db.get_domicilio_id(form["calle"].value, form["sector"].value, form["nombre"].value)
            )
            db.save_mascota_domicilio(data_mascota)

            id_mascota = db.get_mascota_id(form["tipo-mascota"].value, form["edad-mascota"].value, form["color-mascota"].value, \
                db.get_domicilio_id(form["calle"].value, form["sector"].value, form["nombre"].value), form["raza-mascota"].value)

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

                    size = os.fstat(fileitem.file.fileno()).st_size
                    tipo_real = filetype.guess(fileitem.file)
                    if size <= MAX_FILE_SIZE:

                        fn = os.path.basename(fileitem.filename)
                        open('./tmp/'+fn, 'wb').write(fileitem.file.read())
                        mensaje = "El archivo fue recibido correctamente"
                        data_foto = (

                        './tmp/'+fn, fn, id_mascota
                        )
                        db.save_foto_mascota(data_foto)

                    else:

                        mensaje = "El archivo pesa mucho"
                    actual_mascota+=1

                except IOError as e:

                    mensaje = "Error"

            else:

                mensaje = "No se recibio el archivo"
                actual_mascota+=1

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

