def quickSort(alist):
   # call the below recursive method and pass initial values to begin sorting
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   # apply sorting only if last-index is greater than first-index.
   if first<last:
       # call the below method to partition the list and returns the split-point.
       # pass this split-point , first-index and last-index to the current method recursively.
       splitpoint = partition(alist,first,last)

       # call the current method recursively with new parameters.
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   # read the pivot value.
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       # increment the left-index till it is less than the pivot and less than the right-index.
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       # decrement the right-index till it is greater than the pivot and greater than the less-index.
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       # if right and left index crosses each other than stop here, its time to split the list.
       # else swap the values at left and right index.
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   # this is the split point, hence, pivot value will change here by swapping the pivot and value at the right index.
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

# initialize the list.
alist = [54,26,93,17,77,31,44,55,20]
# call the method resposible for sorting based on quick-sort algo.
quickSort(alist)
print(alist)