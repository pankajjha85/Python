ls = [23,44,64,158,12,89,390]

max_num = max(ls)
print('The maximum value among the list is '+ str(max_num) )

# ***********  OR  ******************

ls = [23,44,64,158,12,89,390]

max_value = 0

for item in ls:
    if max_value < item:
        max_value = item
    
print('The maximum value among the list is '+ str(max_value) )