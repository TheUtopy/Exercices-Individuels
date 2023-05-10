function tryWord(word, base) {
	// TODO: fix jeu sensible à la casse.
	if (word === base) {
		return true
  } else {
  	let wellPlaced = [];
    let notInWord = [];
    let missplaced = [];
    
  	let arrayBase = base.split('');
    let arrayWord = word.split('');
    
	for (let i in arrayWord) {
        if (arrayBase[i] === arrayWord[i]) {
      	    wellPlaced.push(arrayWord[i]);
        }	else if (arrayBase.includes(arrayWord[i])) {
            missplaced.push(arrayWord[i])
        } else {
            notInWord.push(arrayWord[i])
        }
    }
    
    return { wellPlaced: wellPlaced, missplaced: missplaced, notInWord: notInWord }
  }
}

function guess() {
	let base = 'dictionnaire'
	let word = document.getElementById("word").value
    word = word.toLowerCase()
	let result = tryWord(word, base)
    document.getElementById("word").value = ''
    document.getElementById("try").innerText = word
    document.getElementById("well").innerText = ""
    document.getElementById("miss").innerText = ""
    document.getElementById("not").innerText = ""
    document.getElementById("win").innerText = ""
  if (result !== true){
    document.getElementById("well").innerText = 'Bien placé: '+result.wellPlaced.join(', ')
    document.getElementById("miss").innerText = 'Mal placé: '+result.missplaced.join(', ')
    document.getElementById("not").innerText = 'Pas dans le mot: '+result.notInWord.join(', ')
  }
  else {
	document.getElementById("win").innerText = 'Vous avez gagné'
  }
}
