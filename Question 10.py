def longest(list1):
    new_set =[] #creates a temporary set to hold values
    complete_set = [] #Contains the new set
    num_start = 0

    for number in range(len(list1)):  #Itterates through the length of the list from element 0
        if number <= 0:
            new_set.append(list1[number]) # If statement appends new numbes equal or less than to the temporary list
        elif list1[number] >= list1[number-1]: # If the previous number is less tan the current it is appended to the temp set
            new_set.append(list1[number])
        elif list1[number] < list1[number-1]: #If the current element is less than the previous the remp set is appended to the completed set
            complete_set.append(new_set)
            new_set = []
            new_set_extract = new_set
            new_set_extract.append(list1[number]) # The element which broke the list is appened to its own set
    

    print(complete_set)

  
            
            
