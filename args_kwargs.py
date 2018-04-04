#! python3

def func_arg(*args):
    print('args = {}'.format(args))
    
    var = 0
    for i in args:
        print('value of paramter [{}] = {}'.format(var,i))
        var +=1

func_arg(1,2,3,4) 

def func_kwarg(**kwargs):
    print('kwargs = {}'.format(kwargs))
    
    for i,j in kwargs.items():
        print('parameter = {} value = {}'.format(i,j))
        
func_kwarg(a=1,b=2)        


    