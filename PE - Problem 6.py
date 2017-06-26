# problem 6, PE - sum square difference

def sumOfSquares(): #finds sum of the squares
    sumCounter = 0
    for i in range(1, 101):
        sumCounter = sumCounter + i**2
        if i == 100:
            return sumCounter

def squareOfSums(): #finds sqaure of the sum
    sumCounter = 0
    for i in range(1, 101):
        sumCounter = sumCounter + i
        if i == 100:
            return sumCounter**2

print(squareOfSums() - sumOfSquares()) #gives output
