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

var numFile = 0;

function addInputFile(num){

    if(numFile<num) {
        var container = document.getElementById("container-file");
        var inputFile = document.createElement("input");
        inputFile.type = "file";
        container.appendChild(inputFile);
        container.appendChild(document.createElement("br"));
        numFile = numFile + 1;
    }
}
var ciudades_1 = ["Arica"];
var ciudades_2 = ["Alto Hospicio","Iquique","Pozo Almonte"];
var ciudades_3 = ["Caldera","Chanaral","Copiapo","Diego de Almagro","El Salvador","Huasco","Tierra Amarilla","Vallenar"];
var ciudades_4 = ["Andacollo","Combarbala","Coquimbo","El Palqui","Illapel","La Serena","Los Vilos","Montepatria","Ovalle","Salamanca","Vicuna"];
var ciudades_5 = ["Algarrobo","Cabildo","Calle Larga","Cartagena","Casablanca","Catemu","Concon","El Melon","El Quisco","El Tabo","Hijuelas","La Calera","La Cruz","La Ligua","Las Ventanas","Limache","Llaillay","Los Andes","Nogales","Olmue","Placilla de Penuelas","Putaendo","Quillota","Quilpue","Quintero","Rinconada","San Antonio","San Esteban","San Felipe","Santa Maria","Santo Domingo","Valparaiso","Villa Alemana","Villa Los Almendros","Vina del Mar"];
var ciudades_6 = ["Chimbarongo","Codegua","Donihue","Graneros","Gultro","Las Cabras","Lo Miranda","Machali","Nancagua","Palmilla","Peumo","Pichilemu","Punta Diamante","Quinta de Tilcoco","Rancagua","Rengo","Requinoa","San Fernando","San Francisco de Mostazal","San Vicente de Tagua Tagua","Santa Cruz"];
var ciudades_7 = ["Cauquenes","Constitucion","Curico","Hualane","Linares","Longavi","Molina","Parral","San Clemente","San Javier","Talca","Teno","Villa Alegre"];
var ciudades_8 = ["Arauco","Bulnes","Cabrero","Canete","Chiguayante","Chillan","Chillan Viejo","Coelemu","Coihueco","Concepcion","Conurbacion La Laja-San Rosendo","Coronel","Curanilahue","Hualpen","Hualqui","Huepil","Lebu","Los alamos","Los angeles","Lota","Monte aguila","Mulchen","Nacimiento","Penco","Quillon","Quirihue","San Carlos","San Pedro de la Paz","Santa Barbara","Santa Juana","Talcahuano","Tome","Yumbel","Yungay"];
var ciudades_9 = ["Angol","Carahue","Collipulli","Cunco","Curacautin","Freire","Gorbea","Labranza","Lautaro","Loncoche","Nueva Imperial","Padre Las Casas","Pitrufquen","Pucon","Puren","Renaico","Temuco","Traiguen","Victoria","Villarrica"];
var ciudades_10 = ["Futrono","La Union","Lanco","Los Lagos","Paillaco","Panguipulli","Rio Bueno","San Jose de la Mariquina","Valdivia"];
var ciudades_11 = ["Coihaique","Puerto Aisen"];
var ciudades_12 = ["Punta Arenas","Puerto Natales"];
var ciudades_13 = ["Alto Jahuel","Bajos de San Agustin","Batuco","Buin","Cerrillos","Cerro Navia","Colina","Conchali","Curacavi","El Bosque","El Monte","Estacion Central","Hospital","Huechuraba","Independencia","Isla de Maipo","La Cisterna","La Florida","La Granja","La Islita","La Pintana","La Reina","Lampa","Las Condes","Lo Barnechea","Lo Espejo","Lo Prado","Macul","Maipu","Melipilla","Nunoa","Padre Hurtado","Paine","Pedro Aguirre Cerda","Penaflor","Penalolen","Pirque","Providencia","Pudahuel","Puente Alto","Quilicura","Quinta Normal","Recoleta","Renca","San Bernardo","San Joaquin","San Jose de Maipo","San Miguel","San Ramon","Santiago","Talagante","Tiltil","Vitacura"];
var ciudades_14 = ["Ancud","Calbuco","Castro","Fresia","Frutillar","Llanquihue","Los Muermos","Osorno","Puerto Montt","Puerto Varas","Purranque","Quellon","Rio Negro"];
var ciudades_15 = ["Antofagasta","Calama","Maria Elena","Mejillones","Taltal","Tocopilla"];

arregloRegiones = [ciudades_1, ciudades_2, ciudades_3, ciudades_4,ciudades_5, ciudades_6, ciudades_7, ciudades_8, ciudades_9, ciudades_10, ciudades_11, ciudades_12, ciudades_13, ciudades_14, ciudades_15]

function buscar_ciudad(){
    var region, i, comunas, j;
    region = document.getElementById("region").value
    var com = document.getElementById("comuna");
    if (region !== 0) {
        comunas = eval("ciudades_" + region);

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


function clonar(id) {
    var c = document.getElementById(id);
    var clon = c.cloneNode(id);
    var principal = document.getElementById("principal-section");
    var botones = document.getElementById("botones-form");
    principal.appendChild(clon);
    principal.appendChild(botones);


}
