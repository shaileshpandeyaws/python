#! python3

class bas():
	count = 0
	def __init__(self, val1,val2):
		self._val1 = val1
		self.__val2 = val2
		bas.count +=1
		
	def hello(self):
		print('hello')
		print(self.__val2)
		
		

obj = bas('1','2')
obj.hello()
print('number of objects {}'.format(bas.count))

obj2 = bas('1','2')
obj2.hello()
print('number of objects {}'.format(bas.count))

obj3 = bas('1','2')
obj3.hello()
print('number of objects {}'.format(bas.count))



		