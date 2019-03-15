def qsort(arr , pivot_index , low , high):
#{
    if len(arr) == 1 or high < 0:
        return arr
    
    while( arr[low] < arr[pivot_index]):
    #{
        low = low + 1
    #}

    while( arr[high] > arr[pivot_index] ):
    #{
        high = high - 1
    #}

    if low < high:
    #{
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        qsort(arr , pivot_index , low , high)
    #}
    else:
    #{
        temp = arr[pivot_index]
        arr[pivot_index] = arr[low]
        arr[low] = temp

        temp_list = qsort( arr[0:low] , high , 0 , high-1 )
        i = 0
        if len(temp_list) > 0:
        #{
            for item in temp_list:
                arr[i] = item
                i = i + 1
        #}
                
        temp_list = qsort( arr[ (low+1): ] , (len(arr[ (low+1): ])-1) , 0 , ((len(arr[ (low+1): ])-1)-1))
        i = (low+1)

        if len(temp_list) > 0:
        #{
            for item in temp_list:
                arr[i] = item
                i = i + 1
        #}
    #}
    return arr
#}

#arr = [35,33,42,10,14,19,27,44,26,31]
#arr = [59,15,45,23,75,46,49,20,57,65]
arr = [106,208,4,61,94,588,2194,230,467,100]

pivot_index = len(arr) - 1
low = 0
high = pivot_index - 1

arr = qsort( arr , pivot_index , low , high )
print(arr)


