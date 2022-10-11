function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

let count = document.getElementById("buttonCountNumber");
document.getElementById("buttonCountPlus").onclick = function () {
    let countPlus = count.innerHTML;
    if (+countPlus <= 19) {
        count.innerHTML++;

    }
}
document.getElementById("buttonCountMinus").onclick = function () {
    let countMinus = count.innerHTML;
    if (+countMinus >= 2) {
        count.innerHTML--;
    }
}

document.getElementById("ggg").onclick = function () {
    axios.get('/dnd/todo/')
        .then(function (response) {
            // обработка успешного запроса
            let lvl = document.getElementById('buttonCountNumber');
            let new_lvl = response.data.lvl;
            lvl.innerHTML = new_lvl;
            console.log(response);
        })
}
