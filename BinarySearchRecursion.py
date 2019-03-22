import math

# create the function to navigate through the list and search the user input.
def search( arr1 , u ):
    # check if length of the array is 2 or 1.
    # if yes, iterate thru each element, compare with the user input, if matched, inform the user.
    # if not matched, inform the user that search not found.
    if len(arr1) == 2:
        if arr1[0] == u or arr1[1] == u:
            print('Search found within the list:')
            print(arr1)
        else:
            print('Search not found')
    elif len(arr1)== 1:
        if arr1[0] == u:
            print('Search found within the list:')
            print(arr1)
        else:
            print('Search not found')
    else:
        # calculate the node position of the array by dividing the length by 2 and taking the floor value.
        node = math.floor(len(arr1)/2)
        # if user input is matched with the node value, inform the user.
        if u == arr1[node] :
            print('Search found at the Node:'+str(u))
        elif u < arr1[node]:   # if user input is less than node value then call this function recursively, pass the list of size 0 to node.
            search( arr1[0:node] , u )
        elif u > arr1[node]:   # if user input is greater then node value call this function recursively, pass the list of size node till length.
            search( arr1[node : ] , u )
        


# create the sorted list.
arr=[2,4,5,7,8,9,12,14,17,19,22,25,27,28,33]

print('The original list is:')
print(arr)

# handle the exception if user inputs a letter or special character etc.
try:
    # accept the user input.
    u = int(input('Enter the number to be searched:'))
    print('User input is:'+str(u))
    # call the function.
    search(arr, u)
except:
    print('Invalid input.')
