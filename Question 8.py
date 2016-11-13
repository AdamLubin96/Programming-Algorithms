def vowel(text):
    vowels = "aeiou"  #Variables containing vowels 
    if len(text)==0:  #Conditional cheacks whether the input contains any elements
        return text
    elif text[0] in vowels: #This loop checks the first elemt of the input against the vowels
        return vowel(text[1:]) #The slice method will remove elemets that meet the condition
    else:   
        return text[0] + vowel(text[1:])  #The recursive program incremnets through the input string one position at a time and checks the character    
