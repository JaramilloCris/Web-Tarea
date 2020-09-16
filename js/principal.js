function hideInput(selectId,inputId){

    var d = document.getElementById(selectId);
    var textSeleted=d.options[d.selectedIndex].text;
    document.getElementById(inputId).hidden = textSeleted !== "Otro";
}

var numFile = 0;

function addInputFile(num){

    if(numFile<num) {
        var container = document.getElementById("container-file")
        var inputFile = document.createElement("input");
        inputFile.type = "file";
        container.appendChild(inputFile);
        container.appendChild(document.createElement("br"));
        numFile = numFile + 1;
    }
}

function clickSub(){

    var button = document.getElementById("subm")
    button.style.background = '#000000'

}


