# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 20:53:34 2018

@author: Pankaj_J
"""

# BUBBLE SORT

original_list = [10,7,4,6,485,87,557,5,1,4,2,8]

first_var = 0
second_var = 0
temp_swap = 0

i=0

sort_again = True

# run this loop untill all the elements in the list is sorted.
# if at any time, the two elements in a list are not sorted, then the variable 
# 'sort_again' will be 'True' and the while loop will run again.
while(sort_again):
#{
    # set this variable to zero
    i = 0
    
    # set this to 'False' because in case all the elements are sorted, the while loop should break.
    sort_again = False

    # iterate thru the list
    for item in original_list:
    #{
        # check if the current position is less than (1-length of list) to avoid fetching the next value which does not exist.
        if i<len(original_list)-1:
        #{
            # if the number at current position is greater than the next position,
            # it means sorting is required. Swap the values and put it back in the list.
            first_var = original_list[i]
            second_var = original_list[i+1]
            if first_var > second_var:
            #{
                temp_swap = second_var
                second_var = first_var
                first_var = temp_swap
                
                original_list[i] = first_var
                original_list[i+1] = second_var
                
                # set this to 'True' so that in the next pass, it should iterate over all the elements again and check if sorting is required.
                sort_again = True
            #}
        #}
        
        # increment the variable so that next position's element can be fetched.
        i=i+1
    #}
#}

print(original_list)