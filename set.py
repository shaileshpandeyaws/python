#! python3
print ('hello')
list = [4,3,2,5,6,7,8,9,1,2,3,4,5,5,7,6]
set1 = set(list)
print ('{} {}'.format(type(set1),set1))



val = set('qwertyuiopaslkdjfgzxvcnvmb<>!@#$%^&*(())_+|')
print(val)
print(type(val))

sp_list = []
str_list = []
for i in val:
    print(i)
    print(type(i))
    if(ord(i) >= 65 and ord(i)<= 122):
        print('string')
        str_list.append(i)
    else:
        print('special')
        sp_list.append(i)
        
print('str_list is {}'.format(str_list)) 
print('sp list is {}'.format(sp_list))

