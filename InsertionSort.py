# insertion sort
ls=[45,25,78,46,95,22,35,10]
counter = 0
min_item = 0
min_item_position = 0
temp = 0
sorted_ls = []

while(True):
#{
    min_item = min(ls)
    min_item_position = ls.index(min_item)
    sorted_ls.append(min_item)
    
    ls.pop(min_item_position)
    
    if len(ls) == 0:
        break
#}    