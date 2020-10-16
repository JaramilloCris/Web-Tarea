#!C:\Users\groso\AppData\Local\Programs\Python\Python37\python.exe


print("Content-type: text/html; charset=UTF-8")
print("")  

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
                    <a href="tabla.py" class="nav-ref"><span class="nav-item"></span>Ver listado de mascotas</a>
                    <a href="estadisticas.py" class="nav-ref"><span class="nav-item"></span>Estadisticas</a>
                </nav>
            </div>
            <div class="container-content">

                <table id="myTable">
                    <tr>
                        <th onclick="sortTable(0)">Fecha Ingreso</th>
                        <th onclick="sortTable(1)">Comuna</th>
                        <th onclick="sortTable(2)">Nombre Calle</th>
                        <th onclick="sortTable(3)">Nombre contacto</th>
                        <th onclick="sortTable(4)">Total Mascotas</th>
                        <th onclick="sortTable(5)">Total fotos</th>
                    </tr>
                    <tr onclick="hrefTable('#popup1')">
                        <td>20/11/2018</td>
                        <td>Puente Alto</td>
                        <td>Pullinque</td>
                        <td>Fernanda</td>
                        <td>1</td>
                        <td>2</td>
                    </tr>
                    <tr onclick="hrefTable('#popup2')">
                        <td>19/10/2018</td>
                        <td>Maipu</td>
                        <td>Rencor</td>
                        <td>Juan</td>
                        <td>8</td>
                        <td>19</td>
                    </tr>
                    <tr onclick="hrefTable('#popup3')">
                        <td>20/08/2018</td>
                        <td>La Florida</td>
                        <td>Vicuña Mackenna</td>
                        <td>Laura</td>
                        <td>17</td>
                        <td>12</td>
                    </tr>
                    <tr onclick="hrefTable('#popup4')">
                        <td>16/01/2018</td>
                        <td>Santiago</td>
                        <td>Alameda</td>
                        <td>Fernando</td>
                        <td>14</td>
                        <td>13</td>
                    </tr>
                    <tr onclick="hrefTable('#popup5')">
                        <td>18/03/2017</td>
                        <td>La Granja</td>
                        <td>Mexico</td>
                        <td>Leonardo</td>
                        <td>6</td>
                        <td>12</td>
                    </tr>
                </table>
            </div>
        </section>
    </div>
        <div id="popup1" class="overlay">
            <div class="popupBody">
                <h2 class="tittle">Información de un censo</h2>
                <a class="cerrar" href="#">&times;</a>
                <div class="popupContent">
                    <p class="font-censo">Región: <span>Metropolitana</span></p>
                    <p class="font-censo">Comuna: <span>Puente Alto</span></p>
                    <p class="font-censo">Calle: <span>Pasaje Pullinque</span></p>
                    <p class="font-censo">N°Calle: <span>01274</span></p>
                    <p class="font-censo">Sector: <span>Andes del Sur</span></p>
                    <hr class="censo">
                    <p class="font-censo">Nombre: <span>Cristobal</span></p>
                    <p class="font-censo">Email: <span>cristobal.jaramillo@gmail.com</span></p>
                    <p class="font-censo">N°Celular: <span>+56931194230</span></p>
                    <hr class="censo">
                    <p class="font-censo">Tipo: <span>Gato</span></p>
                    <p class="font-censo">Edad: <span>3</span></p>
                    <p class="font-censo">Color: <span>Rojo</span></p>
                    <p class="font-censo">Raza: <span>Dragon fuego</span></p>
                    <p class="font-censo">Esterilizado: <span>Si</span></p>
                    <p class="font-censo">Vacunas al día: <span>Si</span></p>
                    <img class="imagen-censo1" src="/img/img320/agus.jpeg" alt="Mascota" id = "mascota1" onclick="showImage('span-mascota1')"><br>
                    <img class="imagen-censo2" src="/img/img320/gato1.jpeg" alt="Mascota" onclick="showImage('span-mascota2')"><br>
                    <img class="imagen-censo3" src="/img/img320/perro.jpg" alt="Mascota" onclick="showImage('span-mascota3')"><br>
                    <span class="img800" id="span-mascota1">
                        <img src="img/img800/agus-800.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota1')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota2">
                        <img src="img/img800/gato1-800.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota2')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota3">
                        <img src="img/img800/perro800.jpg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota3')">&times;</a>
                    </span>
                </div>
            </div>
        </div>
        <div id="popup2" class="overlay">
            <div class="popupBody">
                <h2 class="tittle">Información de un censo</h2>
                <a class="cerrar" href="#">&times;</a>
                <div class="popupContent">
                    <p class="font-censo">Región: <span>Metropolitana</span></p>
                    <p class="font-censo">Comuna: <span>Maipu</span></p>
                    <p class="font-censo">Calle: <span>Pasaje Romanita</span></p>
                    <p class="font-censo">N°Calle: <span>01574</span></p>
                    <p class="font-censo">Sector: <span>Villa Juana</span></p>
                    <hr class="censo">
                    <p class="font-censo">Nombre: <span>Roberto</span></p>
                    <p class="font-censo">Email: <span>roberto.juan@gmail.com</span></p>
                    <p class="font-censo">N°Celular: <span>+569877452</span></p>
                    <hr class="censo">
                    <p class="font-censo">Tipo: <span>Perro</span></p>
                    <p class="font-censo">Edad: <span>2</span></p>
                    <p class="font-censo">Color: <span>Cafe</span></p>
                    <p class="font-censo">Raza: <span>Chimuelo</span></p>
                    <p class="font-censo">Esterilizado: <span>Si</span></p>
                    <p class="font-censo">Vacunas al día: <span>Si</span></p>
                    <img class="imagen-censo1" src="/img/img320/perro1.jpeg" alt="Mascota" onclick="showImage('span-mascota4')"><br>
                    <img class="imagen-censo2" src="/img/img320/perro2.jpeg" alt="Mascota" onclick="showImage('span-mascota5')"><br>
                    <img class="imagen-censo3" src="/img/img320/perro3.jpeg" alt="Mascota" onclick="showImage('span-mascota6')"><br>
                    <span class="img800" id="span-mascota4">
                        <img src="img/img800/perro1.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota4')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota5">
                        <img src="img/img800/perro2-800.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota5')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota6">
                        <img src="img/img800/perro3.jpeg"  class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota6')">&times;</a>
                    </span>
                </div>
            </div>
        </div>
        <div id="popup3" class="overlay">
            <div class="popupBody">
                <h2 class="tittle">Información de un censo</h2>
                <a class="cerrar" href="#">&times;</a>
                <div class="popupContent">
                    <p class="font-censo">Región: <span>Metropolitana</span></p>
                    <p class="font-censo">Comuna: <span>Puente Alto</span></p>
                    <p class="font-censo">Calle: <span>Pasaje Pullinque</span></p>
                    <p class="font-censo">N°Calle: <span>01274</span></p>
                    <p class="font-censo">Sector: <span>Andes del Sur</span></p>
                    <hr class="censo">
                    <p class="font-censo">Nombre: <span>Cristobal</span></p>
                    <p class="font-censo">Email: <span>cristobal.jaramillo@gmail.com</span></p>
                    <p class="font-censo">N°Celular: <span>+56931194230</span></p>
                    <hr class="censo">
                    <p class="font-censo">Tipo: <span>Gato</span></p>
                    <p class="font-censo">Edad: <span>3</span></p>
                    <p class="font-censo">Color: <span>Rojo</span></p>
                    <p class="font-censo">Raza: <span>Dragon fuego</span></p>
                    <p class="font-censo">Esterilizado: <span>Si</span></p>
                    <p class="font-censo">Vacunas al día: <span>Si</span></p>
                    <img class="imagen-censo1" src="/img/img320/gato2.jpeg" alt="Mascota" onclick="showImage('span-mascota7')"><br>
                    <img class="imagen-censo2" src="/img/img320/perro4.jpeg" alt="Mascota" onclick="showImage('span-mascota8')"><br>
                    <img class="imagen-censo3" src="/img/img320/perro5.jpeg" alt="Mascota" onclick="showImage('span-mascota9')"><br>
                    <span class="img800" id="span-mascota7">
                        <img src="img/img800/gato2-800.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota7')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota8">
                        <img src="img/img800/perro4.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota8')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota9">
                        <img src="img/img800/perro5-800.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota9')">&times;</a>
                    </span>
                </div>
            </div>
        </div>
        <div id="popup4" class="overlay">
            <div class="popupBody">
                <h2 class="tittle">Información de un censo</h2>
                <a class="cerrar" href="#">&times;</a>
                <div class="popupContent">
                    <p class="font-censo">Región: <span>Metropolitana</span></p>
                    <p class="font-censo">Comuna: <span>Puente Alto</span></p>
                    <p class="font-censo">Calle: <span>Pasaje Pullinque</span></p>
                    <p class="font-censo">N°Calle: <span>01274</span></p>
                    <p class="font-censo">Sector: <span>Andes del Sur</span></p>
                    <hr class="censo">
                    <p class="font-censo">Nombre: <span>Cristobal</span></p>
                    <p class="font-censo">Email: <span>cristobal.jaramillo@gmail.com</span></p>
                    <p class="font-censo">N°Celular: <span>+56931194230</span></p>
                    <hr class="censo">
                    <p class="font-censo">Tipo: <span>Gato</span></p>
                    <p class="font-censo">Edad: <span>3</span></p>
                    <p class="font-censo">Color: <span>Rojo</span></p>
                    <p class="font-censo">Raza: <span>Dragon fuego</span></p>
                    <p class="font-censo">Esterilizado: <span>Si</span></p>
                    <p class="font-censo">Vacunas al día: <span>Si</span></p>
                    <div>
                    <img class="imagen-censo1" src="/img/img320/perro6.jpeg" alt="Mascota" onclick="showImage('span-mascota10')"><br>
                    <img class="imagen-censo2" src="/img/img320/perro7.jpeg" alt="Mascota" onclick="showImage('span-mascota11')"><br>
                    <img class="imagen-censo3" src="/img/img320/gato3.jpeg" alt="Mascota" onclick="showImage('span-mascota12')"><br>
                    </div>
                    <span class="img800" id="span-mascota10">
                        <img src="img/img800/perro6-800.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota10')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota11">
                        <img src="img/img800/perro7-800.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota11')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota12">
                        <img src="img/img800/gato3-800.jpeg" class="imagen-ampliada" alt="Mascota">
                        <a class="cerrar" onclick="hideImage('span-mascota12')">&times;</a>
                    </span>
                </div>
            </div>
        </div>
        <div id="popup5" class="overlay">
            <div class="popupBody">
                <h2 class="tittle">Información de un censo</h2>
                <a class="cerrar" href="#">&times;</a>
                <div class="popupContent">
                    <p class="font-censo">Región: <span>Metropolitana</span></p>
                    <p class="font-censo">Comuna: <span>Puente Alto</span></p>
                    <p class="font-censo">Calle: <span>Pasaje Pullinque</span></p>
                    <p class="font-censo">N°Calle: <span>01274</span></p>
                    <p class="font-censo">Sector: <span>Andes del Sur</span></p>
                    <hr class="censo">
                    <p class="font-censo">Nombre: <span>Cristobal</span></p>
                    <p class="font-censo">Email: <span>cristobal.jaramillo@gmail.com</span></p>
                    <p class="font-censo">N°Celular: <span>+56931194230</span></p>
                    <hr class="censo">
                    <p class="font-censo">Tipo: <span>Gato</span></p>
                    <p class="font-censo">Edad: <span>3</span></p>
                    <p class="font-censo">Color: <span>Rojo</span></p>
                    <p class="font-censo">Raza: <span>Dragon fuego</span></p>
                    <p class="font-censo">Esterilizado: <span>Si</span></p>
                    <p class="font-censo">Vacunas al día: <span>Si</span></p>
                    <img class="imagen-censo1" src="/img/img320/rana1.jpeg" alt="Mascota" onclick="showImage('span-mascota13')"><br>
                    <img class="imagen-censo2" src="/img/img320/perro8.jpeg" alt="Mascota" onclick="showImage('span-mascota14')"><br>
                    <img class="imagen-censo3" src="/img/img320/perro9.jpeg" alt="Mascota" onclick="showImage('span-mascota15')"><br>
                    <span class="img800" id="span-mascota13">
                            <img src="img/img800/rana1-800.jpeg" class="imagen-ampliada" alt="Mascota">
                            <a class="cerrar" onclick="hideImage('span-mascota13')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota14">
                            <img src="img/img800/perro8-800.jpeg" class="imagen-ampliada" alt="Mascota">
                            <a class="cerrar" onclick="hideImage('span-mascota14')">&times;</a>
                    </span>
                    <span class="img800" id="span-mascota15">
                            <img src="img/img800/perro9-800.jpeg" class="imagen-ampliada" alt="Mascota">
                            <a class="cerrar" onclick="hideImage('span-mascota15')">&times;</a>
                    </span>
                </div>
            </div>
        </div>
</body>
</html>


'''

print(html)
