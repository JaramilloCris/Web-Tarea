// Variables de las regiones para las comunas
var regionesConComunas = {
      1: ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"],
      2: ["Arica", "Camarones", "Putre", "General Lagos"],
      3: ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"],
      4: ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"],
      5: ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"],
      6: ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"],
      7: ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"],
      8: ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"],
      9: ["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"],
      10: ["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ránquil", "Treguaco", "Bulnes", "Chillán Viejo", "Chillán", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay", "Coihueco", "Ñiquén", "San Carlos", "San Fabián", "San Nicolás"],
      11: ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío", "Chillán", "Bulnes", "Cobquecura", "Coelemu", "Coihueco", "Chillán Viejo", "El Carmen", "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Treguaco", "Yungay"],
      12: ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"],
      13: ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"],
      14: ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"],
      15: ["Coihaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O Higgins", "Tortel", "Chile Chico", "Río Ibáñez"],
      16: ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "Antártica", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
}

// Funcion para ordenar la tabla por orden alfabetico
// row: Columna de la tabla que se quiere ordenar
// Por defecto esta para myTable
function sortTable(row){

    var table, rows, x, y, ready, i, shouldSwitch, type, count;
    type = "asc"
    count = 0;
    table = document.getElementById("myTable");
    ready = true;
    while (ready){

        ready = false;
        rows = table.rows;

        for(i = 1; i < (rows.length - 1); i++){

            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[row];
            y = rows[i + 1].getElementsByTagName("TD")[row];

            if(x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase() && type === "asc"){

                shouldSwitch = true;
                break;
            }
            else if(x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase() && type === "desc"){
                shouldSwitch = true;
                break;
            }
        }
        if (shouldSwitch){

            rows[i].parentNode.insertBefore(rows[i+1], rows[i]);
            ready = true;
            count++;
        }
        else if(count === 0 && type === "asc"){
            type = "desc";
            ready = true;
        }
    }
}

function hideInput(selectId,inputId){

    var d = document.getElementById(selectId);
    var textSeleted=d.options[d.selectedIndex].text;
    document.getElementById(inputId).hidden = textSeleted !== "Otro";
}


function addInputFile(num, container){


        var divForm = document.getElementById(container);
        if(divForm.childElementCount < 7){
            var inputFile = document.createElement("input");
            inputFile.type = "file";
            divForm.appendChild(inputFile);
            divForm.appendChild(document.createElement("br"));
    }
}
function buscar_ciudad(){
    var region, i, comunas, j;
    region = document.getElementById("region").value;

    var com = document.getElementById("comuna");
    if (region !== 0) {
        comunas = regionesConComunas[region];
        for(j = 0; j < com.options.length; j++) {
            com.removeChild(com.options[j]);
        }

        for(i=0;i < comunas.length; i++){

            var opt = document.createElement('option');
            opt.appendChild( document.createTextNode(comunas[i]) );
            opt.value = 'option value';
            com.appendChild(opt);
        }
    }
}

function hrefTable(tipo){

    document.location = tipo;
}

function showImage(idImage){

    var popup = document.getElementById(idImage);
    popup.style.visibility = "visible";

}

function hideImage(idImage){

    var popup = document.getElementById(idImage);
    popup.style.visibility = "hidden";
}

var contador = 1;
function clonar(id) {

    let newDiv = document.createElement('div');
    newDiv.className = "container-content"
    newDiv.innerHTML = `
        <h2 style="font-weight: bold">Información de mascota: </h2>
            <div class="input-div">
                <br>
                <select id="raza${contador}" class="select-custom" name="tipo-mascota" onchange="hideInput('raza','text-value')" required>
                    <option value="">Seleccione un tipo</option>
                    <option value="perro">Perro</option>
                    <option value="gato">Gato</option>
                    <option value="pez">Pez</option>
                    <option value="tortuga">Tortuga</option>
                    <option value="hamster">Hámster</option>
                    <option value="loro">Loro</option>
                    <option value="iguana">Iguana</option>
                    <option value="araña">Araña</option>
                    <option value="otro">Otro</option>
                </select>
                <input hidden id="text-value${contador}" name="otro-mascota" class="input-style" size="40" maxlength="40" placeholder="Otro...">
            </div>
            <div class="input-div">
                <input name="edad-mascota" class="input-style" id="id-annos${contador}" placeholder="Edad en años..." min="0">
            </div>
            <div class="input-div">
                <input name="color-mascota" placeholder="Color..." class="input-style" id="id-color${contador}" size="30"  maxlength="30" required>
            </div>
            <div class="input-div">
                <input name="raza-mascota" placeholder="Raza..." class="input-style" id="id-raza${contador}" size="30" maxlength="30" required>
            </div>
            <div class="input-div">
                <label for="id-esterilizado${contador}">Esterilizado:</label>
                <br>
                <select id="id-esterilizado${contador}" class="input-style" name="esterilizado-mascota" required>
                    <option value="">Seleccione opción</option>
                    <option value="si">Sí</option>
                    <option value="no">No</option>
                    <option value="no-aplica">No aplica</option>
                </select>
            </div>
            <div>
                <label for="id-vacunado${contador}">Vacunas al día:</label>
                <br>
                <select id="id-vacunado${contador}" name="vacunas-mascota" class="input-style" required>
                    <option value="">Seleccione opción</option>
                    <option value="si">Sí</option>
                    <option value="no">No</option>
                    <option value="no-aplica">No aplica</option>
                </select>
            </div>
            <div>
                <label for="id-foto${contador}">Foto:</label>

                <br>
                <input name="foto-mascota" id="id-foto${contador}" size="15" type="file" required>
                <button class="button-sub" type="button" id="addFile${contador}" onclick="addInputFile(4, 'container-file${contador}')">Añadir archivos</button>
            </div>
            <div id="container-file${contador}">
            </div>
            <br>
        </div>`

    document.getElementById('form1').appendChild(newDiv);
    contador+=1;



}

