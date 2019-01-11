ls = [23,44,64,158,12,89,390]

total = sum(ls)
print('The total value of the list is '+str(total))

# **************  OR  ********************

ls = [23,44,64,158,12,89,390]

total = 0

for item in ls:
    total = total + item
    
print('The total value of the list is '+str(total))