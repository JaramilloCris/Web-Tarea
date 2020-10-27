function mostrarError(msg){


    let mensajeError = document.getElementById('mensaje-error1');
    mensajeError.innerHTML = msg;
    hrefTable('#popup-error');

}

function validarFormulario(){


    /** @type string */ let region = document.getElementById('region').value;
    /** @type string */ let comuna = document.getElementById('comuna').value;

    if(region === ""){
        mostrarError("Seleccione una Region");
        return false;
    }


    else if(comuna === ""){
        mostrarError("Seleccione una Comuna");
        return false;
    }

    /** @type string*/ let nombreCalle = document.getElementById('id-calle').value;
    if(nombreCalle.length > 250 || nombreCalle === ""){

        mostrarError("Nombre de calle invalida");
        return false;
    }

    /** @type string*/ let numero = document.getElementById('id-numero').value;
    if(numero.length > 20 || numero === ""){

        mostrarError("Numero de calle invalido");
        return false;
    }

    /** @type string */ let sector = document.getElementById('id-sector').value;
    if(sector.length > 100 && sector !== ""){

        mostrarError("Sector invalido");
        return false;
    }

    /** @type string */ let nombre = document.getElementById('id-nombre').value;
    if(nombre.length > 200 || nombre === ""){

        mostrarError("Nombre invalido")
        return false;

    }
    let regexEmail = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g;
    /** @type string */ let email = document.getElementById('id-email').value;
    if(!regexEmail.test(email) || email === ""){

        mostrarError("Email incorrecto");
        return false;
    }

    let regexNumber = /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/;
    /** @type string */ let phoneNumber = document.getElementById('id-celular').value;
    if(!regexNumber.test(phoneNumber) && phoneNumber !== ""){

        mostrarError("Numero de telefono invalido");
        return false;
    }

    let tipo = document.getElementsByName('tipo-mascota');
    let tipoOtro = document.getElementsByName('otro-mascota');
    for(let i = 0; i < tipo.length; i++){

        if (tipo[i].value === ""){
            mostrarError("Seleccione un tipo de mascota");
            return false;

        }
        else if(tipo[i].value === 'otro' && (tipoOtro[i].value === "" || tipoOtro[i].value.length > 40)){

            mostrarError("Otra mascota invalida");
            return false;
        }
    }
    console.log("ghol3");
    let edadAnimal = document.getElementsByName('edad-mascota');
    let regexEdad = /^[0-9]\d*$/
    for(let i = 0; i < edadAnimal.length; i++){

        if(!regexEdad.test(edadAnimal[i].value)){

            mostrarError("Edad de mascota invalida");
            return false;
        }

    }
    let color = document.getElementsByName('color-mascota');
    for(let i = 0; i < color.length; i++){

        if(color[i].value.length > 30){

            mostrarError("Color de mascota invalido");
            return false;
        }
    }

    let raza = document.getElementsByName('raza-mascota');
    for(let i = 0; i < raza.length; i++){

        if(raza[i].value.length > 30){

            mostrarError("Raza invalida")
            return false;
        }
    }
    let esterilizado = document.getElementsByName('esterilizado-mascota');
    for(let i = 0; i < esterilizado.length; i++){

        if(esterilizado[i].value === ""){

            mostrarError("Ingrese un valor para esterilzado");
            return false;
        }
    }
    let vacunas = document.getElementsByName('vacunas-mascota');
    for(let i = 0; i < vacunas.length; i++){

        if(vacunas[i].value === ""){

            mostrarError("Ingrese un valor para vacunas");
            return false;
        }
    }
    let cantidadMascotas = vacunas.length;
    for(let i = 0; i < cantidadMascotas; i++){

        let name = 'foto-mascota' + i.toString();
        let fotos = document.getElementsByName(name);
        let cantidadFotos = 0;
        for(let j = 0; j < fotos.length; j++){

            if(fotos[j].files.length === 1) {
                cantidadFotos += 1;
            }
        }
        if(cantidadFotos === 0){

            mostrarError("Ingrese al menos una foto por mascota");
            return false;
        }


    }

    hrefTable('#popup-validado');
    return true;



}

