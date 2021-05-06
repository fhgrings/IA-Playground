function bestMove(list) {
    var newList = list
    var score
    var result = checkWinner(listToMatrix(newList, 3))
    if (result) alert(result)

    newList.forEach((position) => {
        newList[position] = 1
        score = minimax(newList)
        if (score > bestScore)

        
    })

    var bestScore = Infinity;
    minimax(matrix)
    
}

function minimax(list) {
    var result = checkWinner(list)
    if (resutl) return result

    var possibilites = getPossibilities();

    possibilites.forEach((poss) => {
        
        console.log(poss)
    })
}  

function getPossibilities() {
    var possibilites = [];
    var newList = DOMtolist();
    for (var i=0;i<newList.length;i++) {
        if (newList[i] == 0) {
            possibilites.push(i);
        }    
    }
    console.log(possibilites)

    return possibilites;
}