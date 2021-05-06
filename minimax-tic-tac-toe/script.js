var dict = {
    "axes" : 1,
    "o"    : -1
}
var element;
window.onload = function () {
    element = document.getElementsByClassName("block")
    machinePlay();
}

function clicked(element) {
    if (! element.children[0]) {
        element.innerHTML = '<div class="o">O</div>'
        var result = checkWinner(DOMtolist())
        if (result) alert(result)
        machinePlay();
        return
    }
    return console.error("Ocupado");
}

function machinePlay() {
    // bestMove();
    // var ran = Math.floor(Math.random()*9);
    // if (document.getElementsByClassName("block")[ran].children[0]) {
    //     machinePlay()
    //     return
    // }
    // document.getElementsByClassName("block")[ran].innerHTML = '<div class="axes">X</div>'
    // checkWinner();
    // return
}

function checkWinner(list) {
    var sum = 0;
    var matrix = listToMatrix(list, 3)

    for(var i=0; i<matrix.length; i++) {
        for(var j=0;j<matrix.length;j++) {
            sum += matrix[i][j]
        }
        if(checkPoints(sum) != 0) {
            return checkPoints(sum)
        }
        sum=0
    }

    for(var i=0; i<matrix.length; i++) {
        for(var j=0;j<matrix.length;j++) {
            sum += matrix[j][i]
        }
        if(checkPoints(sum) != 0) {
            return checkPoints(sum)
        }
        sum=0
    }

    for(var i=0; i<matrix.length; i++) {
        sum += matrix[i][i]
    }
    if(checkPoints(sum) != 0) {
        return checkPoints(sum)
    }
    sum=0

    for(var i=0; i<matrix.length; i++) {
        matrix[i].reverse()
    }
    for(var i=0; i<matrix.length; i++) {
        sum += matrix[i][i]
    }
    if(checkPoints(sum) != 0) {
        return checkPoints(sum)
    }
    return
}

function DOMtolist() {
    var list = []
    for (var i=0; i<element.length; i++) {
        if (element[i].children[0])
            list[i] = dict[element[i].children[0].className]
        else 
            list[i] = 0
    }
    return list;
}

function checkPoints(points) {
    if (points == 3) {
        return 1
    }
    if (points == -3) {
        return -1
    }
    return 0
}

function listToMatrix(list, matrixLenght) {
    var matrix = [], i, k;
    for (i = 0, k = -1; i < list.length; i++) {
        if (i % matrixLenght === 0) {
            k++;
            matrix[k] = [];
        }
        matrix[k].push(list[i]);
    }
    return matrix;
}

