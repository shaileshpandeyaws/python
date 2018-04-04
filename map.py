def myFunc(x):
    return (x*x)

myList = [1,2,3]
i=0

var = (map(myFunc,myList))
for i in var:
    print(i)
    
print(list(map(myFunc,myList)))    
 