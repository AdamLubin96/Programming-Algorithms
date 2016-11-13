def trailingZeroes(n): #Creates the function
    base = 1 #Set the base case as 1 which once hit terminates the program   O(1)
    result = 0 #Set a counter for the result, this will increment in relation to the trailing zereos O(1)
    while n >= base: #Conditional is used to check the input against the base case  O(n^2)
        base = base * 5 #multiples of 5 going into the factorial determine how many trailing zeoes there will be   O(n^2)
        result = result + n//base #Final result becomes n divided by the base, but floor divison will round it to a decimal n*5 O(n^2)
    return result #Returns final result    
        
n = 10
print(trailingZeroes(n))
        
