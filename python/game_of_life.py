import numpy as np
import os
import time

def createMatrix(n):
    matrix = np.chararray((30,30), unicode=True)
    matrix[:] = str('-')
    return matrix

def printMatrix(matrix):
    for row in matrix:
        print(' '.join(row))

def setStartingPoints():
    startingPoints = [[5,5], [6,6], [7,6], [7,5], [7,4]]
    for point in startingPoints:
        matrix[point[0], point[1]] = 'o'

def applyRules(matrix):
    matrix2 = matrix.copy()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            n = countLiveNeighbors(np.pad(matrix, 1, pad_with)[row:row+3, col:col+3])
            if matrix[row][col] == 'o':
                if n < 3 or n > 4:
                    matrix2[row][col] = '-'
            else:
                if n == 3:
                    matrix2[row][col] = 'o'
    return matrix2

def pad_with(vector, pad_width, arg1,arg2):
    vector[:pad_width[0]] = '-'
    vector[-pad_width[1]:] = '-'

def countLiveNeighbors(subMatrix):
    total = 0
    for row in subMatrix:
        for col in row:
            if col == 'o':
                total += 1
    return total
    
matrix = createMatrix(10)
os.system('cls' if os.name == 'nt' else 'clear')
setStartingPoints()
while True:
    matrix = applyRules(matrix)
    printMatrix(matrix)
    time.sleep(0.1)