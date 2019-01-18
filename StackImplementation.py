ls_stack = []

while(True):
    user_input_choice = int(input('Enter the choice. 1:PUSH or 2:POP or 3:READ ALL or 4:EXIT.'))
    
    if user_input_choice == 1:
        user_input_push = int(input('Enter the number to push to the Stack.'))
        ls_stack.append(user_input_push)
        
    elif user_input_choice == 2:
        if len(ls_stack) == 0:
            print('No more items to Pop')
        else:
            ls_stack.pop()
            print('The Stack has been popped.')
        
    elif user_input_choice == 4:
        print('The program has been terminated')
        break
    
    print('The latest Stack is ')
    print(ls_stack)