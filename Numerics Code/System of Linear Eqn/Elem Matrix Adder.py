import math as mt
from fractions import Fraction
matrix = [[2, -1, 3, 10], [0.0, -0.5, 0, 0.5], [0.0, 0.0, -46.0, -92.0]]
elem = [[1,0,0],[0,1,0],[0,0,1]]

play = True

while play:
    print('use index')
    x = float(sum(Fraction(s) for s in input("multiplier: ").split()))
    h = int(input("row to multiply: "))
    k = int(input("row to add to: "))


    temp = [i*x+j for i,j in zip(matrix[h],matrix[k])]

    matrix[k] = temp

    for row in matrix:
        print("{: >10} {: >10} {: >10} {: >10}".format(*row))