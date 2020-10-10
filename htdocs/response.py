#!C:\Users\groso\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi
import save_db as sd
from datetime import date

print("Content-type: text/html\r\n\r\n")

form = cgi.FieldStorage()
db = sd.AnimalitosDb("root", "")


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

    
Ingresado correctamente
</body>
</html>

'''

print(html)

data_domicilio = (

    date.today(), int(10101), \
        form["calle"].value, form["numero"].value, \
            form["sector"].value, form["nombre"].value, form["email"].value, \
                form["celular"].value
)

db.save_domicilio(data_domicilio)

data_mascota = (


    int(form["tipo-mascota"].value), \
        int(form["edad-mascota"].value), form["color-mascota"].value, form["raza-mascota"].value, \
            int(form["esterilizado-mascota"].value), int(form["vacunas-mascota"].value), db.get_domicilio_id(form["calle"].value, form["sector"].value, form["nombre"].value)
)

db.save_mascota_domicilio(data_mascota)