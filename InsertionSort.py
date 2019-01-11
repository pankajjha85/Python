# define the function to apply the Insertion Sort on a list.
def ApplyInsertionSort(prm_original_ls , prm_output_ls):
    # define the variables.
    current_item = 0
    next_item = 0
    temp = 0
    
    # swap first 2 numbers if first number is greater than the second one.
    # and reassign the numbers in the output-ls list.
    if len(prm_original_ls) > 2:
        current_item = prm_original_ls[0]
        next_item = prm_original_ls[1]
        
        if current_item > next_item:
            temp = next_item
            next_item = current_item
            current_item = temp
            
            prm_output_ls[0] = current_item
            prm_output_ls[1] = next_item
    
    # iterate thru the every item in the original list.
    for i in range(2, len(prm_original_ls)):
        current_item = prm_original_ls[i] #  read the current value.
        
        for j in range(0 , i): # iterate on the output-ls till current index of the original list.
            if current_item < prm_output_ls[j]: # check if the current item from original list is less than the current item from the output list.
                prm_output_ls.pop(i) # if yes, pop the current item of the original list from the output list.
                prm_output_ls.insert(j , current_item) # insert the current item of the original list to the output list at the current index.
                break # break this inner loop.
    
    # return the modified list.
    return prm_output_ls

original_ls = [45,25,78,46,95,22,35,10]
print('The Original List :')
print(original_ls)

output_ls = [45,25,78,46,95,22,35,10]
output_ls = ApplyInsertionSort(original_ls, output_ls)
print('After applying Insertion Sort :')
print(output_ls)