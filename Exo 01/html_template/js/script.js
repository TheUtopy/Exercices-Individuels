
function askName(){
    var username = prompt("Quel est ton nom ? ");
    var bonjourUsername = "Bonjour " + username + " !";

    document.body.innerHTML += "<h2>" + bonjourUsername + "</h2><br />";
}

function askBirthYear() {
    var userBirthYear = parseInt(prompt("Quelle est ton année de naissance ? "));
    var userBirthMonth = parseInt(prompt("Quelle est le numéro de ton mois de naissance ? "));
    var userAge = 2023 - userBirthYear;
    if (userBirthMonth > 2){
        userAge--
    }

    document.body.innerHTML += "<h3>Tu as " + userAge + " ans.</h3><br />" ;
}

askName()
askBirthYear()