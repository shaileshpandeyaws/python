#!python 3

"""

Traceback (most recent call last):
  File "polymorhism.py", line 11, in <module>
    test(1)
TypeError: test() takes 0 positional arguments but 1 was given


"""

def test(i):
	print('one arg')

def test():
	print ('no args')
	

	
test(1)	
	
