
// Inicializacion del mapa
var mymap = L.map('mapid').setView([-33.4500000, -70.6666667], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(mymap);

let a = fetch("/js/regiones.json")
        .then(response => {
           return response.json();
        })
        .then(data => date(data));

function date(a){

        let xhr = new XMLHttpRequest();
    xhr.open('GET', '/cgi-bin/read_censos.py');
    xhr.send();
    xhr.timeout = 3000;
    xhr.onload = function (data) {

        let messages = JSON.parse(data.currentTarget.responseText);
        var html, marker, imagen_est, imagen_vacunas;

        regiones = Object.keys(a);
        for (let llave of regiones) {

            for (let comunas of a[llave]) {
                console.log(comunas["lat"]);
                let arr = [comunas["lat"], comunas["lng"]];

                if (messages.hasOwnProperty(comunas["name"])){

                    let comuna = comunas["name"];
                    var cantidad_fotos = messages[comuna].length.toString().concat(" Fotos disponibles");
                    marker = L.marker(arr, {title: cantidad_fotos}).addTo(mymap);
                    html = `<div class = "bloque-principal">`;
                    for (let arreglo_comuna of messages[comuna]) {

                        if(arreglo_comuna[3] === 1){
                            imagen_est = "/img/aprobado.png"
                        }
                        else {
                            imagen_est = "/img/denegado.png"
                        }

                        if(arreglo_comuna[2] === 1){
                            imagen_vacunas = "/img/aprobado.png"
                        }
                        else {
                            imagen_vacunas = "/img/denegado.png"
                        }

                        var direccion_imagen = "/".concat(arreglo_comuna[1]);
                        html = html.concat(`
                                    <div class="seccion-foto">
                                        <div>
                                            <img src=${direccion_imagen} width="150" height="150">
                                        </div>
                                        <div class="bloque-texto-foto">
                                            <a class="texto-foto">Tipo de mascota: </a><a>${arreglo_comuna[0]}</a><br>
                                            <a class="texto-foto">Edad: </a><a>${arreglo_comuna[6]}</a><br>
                                            <a class="texto-foto">Color: </a><a>${arreglo_comuna[5]}</a><br>
                                            <a class="texto-foto">Raza: </a><a>${arreglo_comuna[4]}</a><br>
                                            <a class="texto-foto">Esterilizado: </a><img src=${imagen_est} width="15" height="15"><br>
                                            <a class="texto-foto">Vacunas: </a><img src=${imagen_vacunas} width="15" height="15"><br>
                                            <a class="texto-foto" href="">Ver Censo</a>
                                        </div>
                                    </div>
                                `)
                    }
                    html = html.concat("</div>");
                }
                else{
                    marker = L.marker(arr, {title: "0 Fotos disponibles"}).addTo(mymap);
                    html = `No hay censos disponibles`;

                }
                marker.bindPopup(html);
            }
        }
    }
}











