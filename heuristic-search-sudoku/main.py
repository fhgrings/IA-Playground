from time import sleep
import os
from heuristic import Sudoku

fronteira = [Sudoku(file="sudoku1.txt", readFile=True, isHeuristic=True)]
count = 0
while (len(fronteira) > 0):
    count += 1
    sudoku = fronteira.pop(0)
    if (sudoku.checkWin()):
        _ = os.system('clear')
        print("--- FIM ---")
        print("Count ",count)
        print(sudoku.toString())
        break
    sudokuList = sudoku.nextSudokus()
    for su in sudokuList:
        _ = os.system('clear')
        print("\nCount ",count)
        print(su.toString())
        sleep(0.1)
        fronteira.append(su)
