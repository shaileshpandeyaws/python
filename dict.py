#! python3

dict = {'1':'a','2':'b'}

for key in dict.keys():
    print('key is {}'.format(key))
for val in dict.values():
    print('value is {}'.format(val))

if '1' in dict.keys():
    print('key value pair {}:{}'.format('1',dict['1']))

print('length is {}'.format(len(dict)))

print(dict.items())

for i,j in dict.items():
    print('i : j {} : {}'.format(i,j))

l =dict.items()
print(type(l))



dict2 = dict.copy()
print('dict 2 {}'.format(dict2))

#dict.clear()
#print(dict)

del dict

print('dict 2 after dict 1 deleted {}'.format(dict2))

print('print dict after deleting {}'.format(dict))

# single key multiple values, vice versa not allowed
z =[1,2,3]

var = {'a': z}

print(var)

for i,j in var.items():
    print('i {} ,j {} '.format(i,j))

    i=0
    for l in j:
        print('list[{}] :  {}'.format(i,l))
        i=i+1
