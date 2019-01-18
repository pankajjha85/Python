
def ValidateParentheses(prm_line):
    # start of function.
    list_of_open_brackets = ['(' , '[' ]
    list_of_closed_brackets = [ ')' , ']' ]
    
    total_open_closed_brackets = 0
    is_bracket_exist = False
    
    for each_item in prm_line:
        if each_item in list_of_open_brackets:
            total_open_closed_brackets = total_open_closed_brackets + 1
            is_bracket_exist = True

        elif each_item in list_of_closed_brackets:
            total_open_closed_brackets = total_open_closed_brackets - 1
    
    if is_bracket_exist == True and total_open_closed_brackets == 0:
        print('The number of open brackets is equal to number of closed brackets. Hence the statment '+ prm_line +' is Valid.')
    elif is_bracket_exist == True and total_open_closed_brackets > 0:
        print('The number of open brackets is Not equal to number of closed brackets. Hence the statment '+ prm_line +' is Not Valid.')
    elif is_bracket_exist == False and total_open_closed_brackets == 0:
        print('No brackets found in the statment '+prm_line)
    
    # end of this function

line1 = '((A+B)+(C-D)'
ValidateParentheses(line1)
line2 = '((A+B)+[C-D])'
ValidateParentheses(line2)
line3 = 'A+B-C+D'
ValidateParentheses(line3)
