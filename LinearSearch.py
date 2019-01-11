lst = [23,44,34,76,123,432,898,669,445,2567,660]

num_to_search = int( input('Enter the number to search.') )

search_successful = False

for item in lst:
#{
    if item == num_to_search:
    #{
        print('The search is successful.')
        search_successful = True
        break
    #}
#}
    
if search_successful == False:
#{
    print('The number entered by you does not exists in the List.')
#}