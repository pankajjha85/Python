
def ManageQueue(que):
    # assogn the default value to the user-choice
    user_choice = 0

    # iterate till user enters 3 to exit the application.    
    while(True):
        # request user choice. 1 for Enqueue, 2 for Dequeue, 3 for Exit.
        user_choice = int(input('Enter the choice, 1 for Enqueue, 2 for Dequeue or 3 for Exit.'))
        
        # if user enters 3, break the loop.
        if user_choice == 3:
            print('Application is terminated')
            break
        elif user_choice == 1:   # if the choice is 1, ask the value to enter and add it to the list.
            user_input = int(input('Enter the value to Enqueue.'))
            que.append(user_input)
        elif user_choice == 2:     # if the choice is 2, remove the value from the list at the first position.
            if len(que) == 0:      # before removing the value from the list, check if the list is non-empty.
                print('No more element for Dequeue.')
            else:
                que.remove(que[0])  # remove the element from the first position from the list.
                
        # print the latest queue.
        print('The latest values in Queue are :')
        print(que)


# initially the queue will be blank
que = []
ManageQueue(que)