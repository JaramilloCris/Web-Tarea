function hideInput(selectId,inputId){

            var d = document.getElementById(selectId);
            var textSeleted=d.options[d.selectedIndex].text;
            document.getElementById(inputId).hidden = textSeleted !== "Otro";
        }