from math import sqrt, inf

class Sudoku():
    def __init__(self, matrix=None, file=None, readFile=False, isHeuristic=False):
        if readFile:
            f = open(file, "r")
            matrix = []
            for line in f:
                if line[0] == "-":
                    continue
                line = line.replace("\n", "")
                line = line.replace("_","0")
                line = line.replace("|", " ")
                line = line.split(" ")
                line = [([int(i),inf] if i != '0' else [int(i), 0]) for i in line]
                matrix.append(line)
        self.matrix = matrix.copy()
        self.nextZero = self.getNextZero()
        self.nextMove = [0,0]
        self.squareLenth = int(sqrt(len(self.matrix)))
        self.isHeuristic = isHeuristic
        if self.isHeuristic:
            self.evaluatePriority()

    def evaluatePriority(self):
        while self.nextZero:
            possSize = len(self.getPossibilities(self.nextZero))
            self.matrix[self.nextZero[0]][self.nextZero[1]] = [10,possSize]
            self.nextZero = self.getNextZero()
        for x in range(0,len(self.matrix)):
            for y in range(0,len(self.matrix)):
                if self.matrix[y][x][0] == 10:
                    self.matrix[y][x][0] = 0
        self.nextZero = self.getNextZero()
        return 

    def __usedToFree(self, valUsed):
        response = []
        for val in range(1,(len(self.matrix)+1)):
            if not (val in valUsed):
                response.append(val)
        return response

    def __getSquarePossibilities(self, X, Y):
        valUsed = []
        for x in X:
            for y in Y:
                if self.matrix[y][x][0] != 0:
                    valUsed.append(self.matrix[y][x][0])
        return self.__usedToFree(valUsed)

    def __getLinePossibilities(self, y):
        valUsed = []
        for i in range(0,len(self.matrix)):
            if self.matrix[y][i][0] != 0:
                valUsed.append(self.matrix[y][i][0])
        return self.__usedToFree(valUsed)

    def __getColumnPossibilities(self, x):
        valUsed = []
        for i in range(0,len(self.matrix)):
            if self.matrix[i][x][0] != 0:
                valUsed.append(self.matrix[i][x][0])
        return self.__usedToFree(valUsed)
    
    def checkWin(self):
        if not (self.nextZero):
            return True
        return False

    def getNextMove(self):
        response = []
        minPosibilities = len(self.matrix)+1
        for x in range(0,len(self.matrix)):
            for y in range(0,len(self.matrix)):
                if self.matrix[x][y][1] < minPosibilities:
                    if self.matrix[x][y][0] == 0:
                        minPosibilities = self.matrix[x][y][1]
                        response = [x,y]

        self.matrix[response[0]][response[1]][1] = inf
        return response

    def getNextZero(self):
        for x in range(0,len(self.matrix[0])):
            for y in range(0,len(self.matrix)):
                if self.matrix[x][y][0] == 0:
                    return x,y
        return []

    def checkSquareFromAx(self, matrixPosition):
        square = []
        for ax in matrixPosition:
            arr = []
            arr.append(ax)
            copy = ax
            copy+=1
            while (copy%self.squareLenth != 0):
                arr.append(copy)
                copy+=1
            copy = ax
            if (copy%self.squareLenth == 0):
                square.append(arr)
                continue
            while (copy%self.squareLenth != 0):
                copy-=1
                arr.append(copy)
            square.append(arr)
        return square

    def getPossibilities(self, move):
        Ysquare, Xsquare = self.checkSquareFromAx(move)
        square = self.__getSquarePossibilities(Xsquare, Ysquare)
        line = self.__getLinePossibilities(move[0])
        column = self.__getColumnPossibilities(move[1])

        return list(set(square) & set(line) & set(column))

    def nextSudokus(self):
        self.nextMove = self.getNextMove()
        response = []
        possibilitiesList = self.getPossibilities(self.nextMove)
        for possibilitie in possibilitiesList:
            newMatrix = self.matrix
            newMatrix[self.nextMove[0]][self.nextMove[1]][0] = possibilitie
            if self.isHeuristic:
                sudoku = Sudoku(self.copyList(newMatrix), isHeuristic=True)
            else:
                sudoku = Sudoku(self.copyList(newMatrix))
            response.append(sudoku)
        return response

    def toString(self):
        print("\n----------+-----------+------------")
        for y in range(0, len(self.matrix)):
            for x in range(0, len(self.matrix)):
                print(self.matrix[y][x][0], end=" | ")
            if ((y+1)%3 == 0):
                print("\n----------+-----------+------------")
            else:
                print("")

    def copyList(self, newMatrix):
        yy = []
        tt = []
        for x in range(0, len(newMatrix)):
            for y in range(0, len(newMatrix)):
                yy.append([newMatrix[x][y][0],newMatrix[x][y][1]])
            tt.append(yy)
            yy = []
        return tt


