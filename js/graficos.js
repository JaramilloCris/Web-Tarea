function readCensos() {

    // Esta funcion lee la cantidad de censos realizados por dia y genera un grafico
    // a partir de esos datos

    console.log('Cargando mensajes desde el servidor');
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/cgi-bin/read_date.py');
    xhr.send();
    xhr.timeout = 3000;
    xhr.onload = function (data) {

        console.log(data);
        let messages = JSON.parse(data.currentTarget.responseText);
        console.log(messages);
        new Chart(document.getElementById("censos-diarios"), {
            type: 'line',
            data: {
                labels: messages[0],

                datasets: [
                    {
                        label: "Cantidad Censos",
                        borderColor: 'blue',
                        backgroundColor: "transparent",
                        data: messages[1]
                    }
                ]
            },
            options: {
				responsive: true,
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        },
                      scaleLabel: {
                        display: true,
                        labelString: 'Cantidad'
                      }
                    }],
                    xAxes: [{
                      scaleLabel: {
                        display: true,
                        labelString: 'Año - Mes'
                      }
                    }]
                  }
			}
        });
    }
}


colors = [];
function getRandomColor() {

    // Esta funcion se encarga de generar un color aleatorio para el grafico
    // de torta

    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function readMascotas(){

    // Lee la cantidad que hay de cada una de las mascotas disponibles en la base de datos
    // Y genera un grafico de torta a partir de ellos

    console.log('Cargando mensajes desde el servidor');
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/cgi-bin/read_mascotas.py');
    xhr.send();
    xhr.timeout = 3000;
    xhr.onload = function (data) {

        console.log(data);
        let messages = JSON.parse(data.currentTarget.responseText);
        console.log(messages);
        while (colors.length !== messages[0].length){

            colors.push(getRandomColor());

        }
        new Chart(document.getElementById("cantidad-mascotas"), {
            type: 'pie',
            data: {
                labels: messages[0],

                datasets: [
                    {
                        label: "Cantidad Censos",
                        backgroundColor: colors,
                        data: messages[1]
                    }
                ]
            },
            options: {
				responsive: true,
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
			}
        });
    }
}

function read_gatos_perros(){

    // Esta funcion lee la cantidad de perros y gatos por mes y año y los
    // Muestra en un grafico

    console.log('Cargando mensajes desde el servidor');
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/cgi-bin/read_gatos_perros.py');
    xhr.send();
    xhr.timeout = 3000;
    xhr.onload = function (data) {

        console.log(data);
        let messages = JSON.parse(data.currentTarget.responseText);
        console.log(messages);
        new Chart(document.getElementById("gatos-perros"), {
            type: 'bar',
            data: {
                labels: messages[0],

                datasets: [
                    {
                        label: "Cantidad Perros",
                        backgroundColor: "rgb(255,0,0,0.7)",
                        data: messages[1]
                    },
                                     {
                        label: "Cantidad Gatos",
                        backgroundColor: "rgb(0,0,255,0.8)",
                        data: messages[2]
                    }
                ]
            },
            options: {
				responsive: true,
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
                scales: {
                    yAxes: [{
                      scaleLabel: {
                        display: true,
                        labelString: 'Cantidad'
                      }
                    }],
                    xAxes: [{
                      scaleLabel: {
                        display: true,
                        labelString: 'Año - Mes'
                      }
                    }]
                  }
			}
        });
    }
}


function initApp(){

    // Funcion llamada en el onload del html

    readCensos();
    readMascotas();
    read_gatos_perros();

}