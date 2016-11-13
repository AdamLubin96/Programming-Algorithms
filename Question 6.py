def String_Reverse():
    sentence = "This is Awesome" #Input string
    sentence = sentence.split()
    Reversed = [] #Empty set for new string
    for character in sentence:
        Reversed.insert(0,character) #Takes last elemnt of the temporary lsit and moves if to the first position.
    return " ".join(Reversed) #Converts the list back into a string format
    
