# Selection sort

# a function to apply selection sort algorithm on the above list.
def ApplySelectionSort(prm_ls):
    # initialize the variables
    min_item = 0
    min_item_position = 0
    
    # we will keep adding the smallest number from the above list to the below list.
    sorted_ls = []
    
    # keep iterating the loop and break on a specific condition
    while(True):
    
        # find the smallest number from the original list.
        min_item = min(prm_ls)
        
        # find the position of the above number from the original list.
        min_item_position = prm_ls.index(min_item)
        
        # add this number to the different list. this way it will be always sorted.
        sorted_ls.append(min_item)
        
        # remove the above number from the original list to remove the duplicacy.
        prm_ls.pop(min_item_position)
        
        # check if length of the original list is 0, it means that all the items...
        # has been added to the different list in a sorted manner. hence exit the loop.
        if len(prm_ls) == 0:
            break
    
    
    # return the sorted list
    return sorted_ls

# initialize an unordered list
original_ls = [45,25,78,46,95,22,35,10]
print('The Original List : ')
print(original_ls)

sorted_ls = ApplySelectionSort(original_ls)
print('After applying the Selection Sort :')
print(sorted_ls)