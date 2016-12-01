import math

def Perfect_Square():
    n = int(input("Enter an interger ")) #Takes input as an integer
    sqrt = math.sqrt(n) #Uses square root function from math to retrieve value for the square
    convert = int(sqrt) #Rounds from float to int as it needs to be a whole number
    higher_Square = convert * convert #The square root to the power of itself will retrieve a perfect square
    lower_Square = (convert +1)**2 #Lower square is set by multiplying the square root by itself and adding 1
    if n-higher_Square > lower_Square-n:
        print("Its square root is " + (str(sqrt)))
        print("Is not a perfect square but the lowest and nearest is") #If the input is not a perfects square, this will run
        return higher_Square
    else:
        print("Its square root is " + (str(sqrt))) #If input is a perfect square, this will run
        print("Is a perfect square ")
        return higher_Square
        
