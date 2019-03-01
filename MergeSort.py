def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        # split the list into two and call this current function recursively.
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # pass the left half list to the current function recursively.
        mergeSort(lefthalf)
        # pass the right half list to the current function recursively.
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        
        # merge the list.
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        # create the left half of the list.
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        # create the right half of the list.
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
