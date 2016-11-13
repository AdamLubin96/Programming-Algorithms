import random #Imports the random module

def List_Random(List):
    #Creates a function which takes 1 parameter in the form of a list             
    New_List = []
    #An empty class variable is created here, this while contain the new random lsit   O(n)
    while len(List) > 0:
        #Conditional checks length of list is greater than zero so changes can actually be made  O(n)
        num = random.randrange(len(List))
        #Num variable is assigned to each element and takes a random element from the list's range O(n)
        New_List.append(List.pop(num))
        #Creates new list by removing random elements from the old list and appending them to the new list. #This is recursive until the list is becomes less than 0 at which point the new list is formed. O(n)


                                   
    return New_List #Returns thew list 

List = [1,2,3,4,5,]
print(List_Random(List))

