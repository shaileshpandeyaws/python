#! python3
listed = [1,2,3,4,'1','B','#','D','@']
print(listed)
#for value in listed:
#    print(value)
print('\n')
#for var in range(len(listed)):
#    print(listed[var])
    
for var in range(len(listed)):
    if(type(listed[var]) == int):
        print('int: ',sep = '\t')
        print(listed[var])
        listed[var] = listed[var] + 10
    if(type(listed[var]) == str):
        print('Str: ',sep = '\t')
        print(listed[var])
        if(listed[var].isalpha()):
            if(listed[var].isupper()):
                listed[var] = listed[var].lower()
            else:
                listed[var] = listed[var].upper()
        elif(listed[var].isalnum()):
            print('no conversion {}'.format(listed[var]))
        else:
            print('special character {}'.format(listed[var]))
            
        
print (listed)       