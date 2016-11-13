def prime(n,d=2):
    print(n,d) #prints incremnets until the program stops
    if d >= n: #If statement cheacks if the divisable is greater than input number.
        print(n)
        print("is a prime number")
        return "Or input was either 1 or 0" #The program will stop when the divisible equal to the number at which case it must be prime.
    elif n == 2: #Two is the first prime number so counter starts here
        print(n)
    elif (n%d) == 0:
        return "is not a prime number" #Any neumber that is divisbile by a number that is 2 or greater is not a prime so the program will stop.
    else:
        return prime(n, d+1) #The recursion begins here wherby d which was 2 will dow become 3 and the program will run again.
        
