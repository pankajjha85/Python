# function to manage Circular Queue.
def ManageCircularQueue(cq):
    front = 0    # initially frot position and rear position in the circular queue will at first position, i.e. 0.
    rear = front
    
    # iterate till user choose to terminate the application.
    while(True):
        user_choice = int(input('Enter the choice, 1 for Enqueue, 2 for Dequeue, 3 for Exit.'))
        
        # if choice is 3, break the loop.
        if user_choice == 3:
            print('Application is terminated.')
            break
        elif user_choice == 1:
            if (rear > 0 and rear < cq_size) or (rear == 0):  # add the element only if the rear position is 0 or it is less than the queue size.
                user_input = int(input('Enter the value to Enqueue.'))
                cq.append(user_input)
                rear = rear + 1       # increment the rear position.
            elif rear == cq_size:  # if rear position is equal to the queue size, then notify the user that queue is full and elmenet cannot be added.
                print('The Circular Queue is full, Enqueue failed.')
        elif user_choice == 2:   # if the choice is 2, then before dequeue check if queue is having any element remaining, else notify the user.
            if len(cq) == 0:
                print('No more elements for Dequeue.')
            else:
                cq.remove(cq[front])   # dequeue the element and decrement the rear position.
                rear = rear - 1
                
        # print the latest queue elements.
        print('The latest Circular Queue is :')
        print(cq)
        

cq = []
cq_size = int(input('Enter the Size of the Circular Queue.'))
ManageCircularQueue(cq)