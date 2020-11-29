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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <script src="/js/graficos.js"></script>

    

</head>
<body class="main" onload="initApp()">

    <div class="principal-container mx-auto">

        <header class="principal-header text-center">
            <h1 class="titulo">Estadisticas</h1>
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
                <div class="imagen-graficos">
                    <h2 class="tittle">Grafico de censos diarios</h2>
                    <canvas id="censos-diarios"></canvas>
                </div>

                <hr class="new">
                <div class="imagen-graficos" style="width: 50%; left: 27%">
                    <h2 class="tittle">Grafico de los distintos tipos de mascotas</h2>
                    <canvas id="cantidad-mascotas"></canvas>
                </div>
                <hr class="new">
                <div class="imagen-graficos">
                    <h2 class="tittle">Grafico de Perros v/s Gatos</h2>
                    <canvas id="gatos-perros"></canvas>
                </div>
            </div>
        </div>
    </div>
</body>

</html>

'''

print(html)