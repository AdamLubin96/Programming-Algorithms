def search(list1, low, high):
    first_element = 0 #Variable set for first elemnt in list
    last_element = len(list1)-1 #variable set for last element in list

    while first_element <= last_element: 
        middle = (first_element + last_element)//2 #finds median value, by taking the sum of the last and first element and dividing by 2
        if list1[middle] > low and list1[middle] < high: #returns true if value sits between low and high inputs
            return True
        elif high and low < list1[middle]:
            last_element = middle - 1   # moves lower down the list if range is greater than middle value
        else:

            first_element = middle + 1   # moves higher up the list if ranges is greater than middle value
    return False        

list1 = [1,2,3,4,5,6,7,8,9]
low = 3
high = 8
print(search(list1,low,high))
