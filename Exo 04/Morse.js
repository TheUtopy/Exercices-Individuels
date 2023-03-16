// Exercice sur du décodage de morse



//Latin => Morse

// Créé une liste de charactères à partir d'une string
function getLatinCharacterList(text)
{
    let listOfCharacter = [];
    for (let i of text)
    {
        listOfCharacter.push(i);
    }

    return listOfCharacter;
}


// Dictionnaire qui référence la trad de chaque charactère en morse
const latinToMorse = {
	'A':'.-',
	'B':'-...',
	'C':'-.-.',
	'D':'-..',
	'E':'.',
	'F':'..-.',
	'G':'--.',
	'H':'....',
	'I':'..',
	'J':'.---',
	'K':'-.-',
	'L':'.-..',
	'M':'--',
	'N':'-.',
	'O':'---',
	'P':'.--.',
	'Q':'--.-',
	'R':'.-.',
	'S':'...',
	'T':'-',
	'U':'..-',
	'V':'...-',
	'W':'.--',
	'X':'-..-',
	'Y':'-.--',
	'Z':'--..'
};


//Fonction qui traduit un charactère Latin=>Morse
function translateLatinCharacter(char)
{
    return latinToMorse[char];
}

// Vérifie si un character est une lettre
function isLetter(str) {
    return str.length === 1 && str.match(/[a-z]/i);
}


// Traduit du texte en  utilisant les autres fonctions
function encode(text)
{
    text = text.toUpperCase();

    let listOfChar = getLatinCharacterList(text);

    let translatedLatin = "";

    for (let char of listOfChar)
    {
        if (isLetter(char))
        {
            translatedLatin += translateLatinCharacter(char);
        }
    }

    return translatedLatin;
}

function latinToMorseOnClick() {
    let text = document.getElementById('Latin').value;
    text = encode(text)
    document.getElementById('Morse').value = text;
}

console.log(encode("Hello, World"))

//Morse => Latin

// Return une liste de charactère en morse
function getMorseCharacterList(text)
{
    return text.split("/");
}

//Dic qui a toutes les trad des char Morse en Latin
const morseToLatin = {
    '-': "T",
    '--': "M",
    '---': "O",
    '--.': "G",
    '--.-': "Q",
    '--..': "Z",
    '-.': "N",
    '-.-': "K",
    '-.--': "Y",
    '-.-.': "C",
    '-..': "D",
    '-..-': "X",
    '-...': "B",
    '.': "E",
    '.-': "A",
    '.--': "W",
    '.---': "J",
    '.--.': "P",
    '.-.': "R",
    '.-..': "L",
    '..': "I",
    '..-': "U",
    '..-.': "F",
    '...': "S",
    '...-': "V",
    '....': "H"
}

//Fonction qui traduit un char Morse=>Latin
function translateMorseCharacter(char)
{
    return morseToLatin[char];
}

//Traduit le texte Morse=>Latin
function decode(text)
{
    let listOfChar = getMorseCharacterList(text)

    let translatedMorse = ""

    for (let char of listOfChar)
    {
        translatedMorse += translateMorseCharacter(char)
    }

    return translatedMorse
}

function morseToLatinOnClick() {
    let text = document.getElementById('Morse').value;
    text = decode(text)
    document.getElementById('Latin').value = text;
    console.log(text)
}



console.log(decode("..../..-/.../---"))
