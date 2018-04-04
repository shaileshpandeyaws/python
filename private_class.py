#! python3

class bas():
	def __init__(self, val1,val2):
		self._val1 = val1
		self.__val2 = val2
		
	def hello(self):
		print('hello')
		print(self.__val2)

obj = bas('1','2')
obj.hello()
print(obj._val1)
print(obj._bas__val2) # accessing private variable outside class

		