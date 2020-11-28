


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

    regiones = Object.keys(a);
    cantidad_regiones = regiones.length;
    for (let llave of regiones){

        for (let comunas of a[llave]){
            console.log(comunas["lat"]);
            let arr = [comunas["lat"], comunas["lng"]];
            var marker = L.marker(arr).addTo(mymap);
            var html =`
                        <div class = "bloque-principal">
                            <div class="seccion-foto">
                                <div>
                                    <img src="http://localhost:8000/img/img.jpeg" width="150" height="150">
                                </div>
                                <div class="bloque-texto-foto">
                                    <a class="texto-foto">Tipo de mascota: </a><a>Perro</a><br>
                                    <a class="texto-foto">Edad: </a><a>Perro</a><br>
                                    <a class="texto-foto">Color: </a><a>Perro</a><br>
                                    <a class="texto-foto">Raza: </a><a>Perro</a><br>
                                    <a class="texto-foto">Esterilizado: </a><a>Imagen</a><br>
                                    <a class="texto-foto">Vacunas: </a><a>Imagen</a><br>
                                    <a class="texto-foto" href="">Ver Censo</a>
                                </div>
                            </div>
                        </div>
                        `
            marker.bindPopup(html);
        }

    }

}











