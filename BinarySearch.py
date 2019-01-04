import math

# create a list of numbers.
ls = [20,30,40,50,80,90,100,125,140,160,190]

# store the above list in one more list so that we can make the changes to this one and the original will remain intact.
temp_ls = ls

# get the input from the user.
user_input = int(input('Enter the number to search.'))

# create this variable which can help us identify if search completed or no.
# by default keep this as False. 
# once the search will be successful, change the valua to True.
search_found = False

# this loop will keep running until either the search is found or the length of the list got reduced to less than 3.
while( search_found == False and len(temp_ls) >= 3 ):
    # calculate the median/center position of the list.
    median = math.floor( len(temp_ls)/2 )
    
    # check if the user-input number is equal to the number at the median position in the list.
    if user_input == temp_ls[median]:
        # if yes, print the message to the user and change the search variable to True so that the loop can break.
        position = ls.index(user_input)
        print('The entered number successfully found at the position ' + str(position+1) +' in the list.')
        search_found = True
    elif user_input < temp_ls[median]: # check if user-input number is less than the number at the median position.
        # if yes, ignore the right hand side of the list and shrink the list starting from the 1st position till median position.
        temp_ls = temp_ls[0 : median]
    elif user_input > temp_ls[median]: # check if user-input is greater than the number at the median position.
        # if yes, ignore the left side of the list and shrink the list starting from the median position to the last element.
        temp_ls = temp_ls[median : len(temp_ls)]
        
    # keep repeating the entire process untill one of the following occurs.
    # 1. if search found, this loop will break.
    # 2. or if the size of the list has come to 1 or 2, then there we cant split it further.
        

# if the above loop is finished and the search is still False, then check the size of the list.
if search_found == False:
    # check if the size of the list is less than 3.
    if len(temp_ls) < 3:
        # iterate thru the list one by one and compare the user-input against each item.
        for item in temp_ls:
            # if matched, then get the position from the original list.
            if item == user_input:
                position = ls.index(user_input)
                # prompt the user about the successful search and change the variable to True.
                print('The entered number successfully found at the position ' + str(position+1) +' in the list.')
                search_found = True
                # break this loop as no need to search further.
                break
        
        # check if search is still False, it means the entered number does not exist in the list.
        if search_found == False:
            print('The entered number could not be found in the List, please refine your search')
