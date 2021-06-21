$(document).ready(function () {

    const url = "http://localhost:8000/app_v2/api-oro"
    
    $.get(url, function (data) {
        console.log(data)

        $("#retiro").click(function () {
            alert("Retiraste tu dinero! son $ " + data.oro_data + " Oros" + data.hola)
        });

    });

});