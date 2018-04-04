def myFunc(x):
    return (x%2 == 0)

myList = [1,2,3,4,5,6,7,8]
i=0

var = (filter(myFunc,myList))
for i in var:
    print(i)
    
print(list(filter(myFunc,myList)))    
 