#! python3

class animal():
	specie = 'animalsss'
	# can be accessed using classname.varname animal.specie

	def __init__(self,family='none',color='none'):
		self.family = family
		self.color = color
		self.name = 'none'
		
	def species(self):
		if(self.family == 'dog'):
			self.name = 'tommy'
		elif(self.family == 'cat'):
			self.name = 'alice'
		elif(self.family == 'rat'):
			self.name = 'scabbers'
		else:
			self.name = 'chipmunk'
				
	def get_color(self):
		return self.color
		
	def get_name(self):
		return self.name + ' ' + self.family

#obj = animal('cat','grey')

#obj.species()
		
#print('type of  species: {}  \nname: {} \ncolor: {} color'.format(obj.specie,obj.get_name(),obj.get_color()))


class Dog(animal):
	def __init__(self, family='none',color='none' , breed = 'domesticated', patches ='False'):
		animal.__init__(self,family,color)
		self.breed = breed
		self.patches = patches
		self.sound = ''
	
	def get_breed(self):
		return (animal.specie)

				
	def set_dog_sound(self,sound):
		self.sound = sound
		
	def get_dog_sound(self):
		return self.sound
		
	def __str__(self):
		return ('string rep of object')
		
	def __len__(self):
		return len('length of object')
		
	def get_color(self):
		return self.color + '  patches (' + str(self.patches) + ')'
		
	
objNew = Dog('dog','black','doberman','No')	

objNew.species()

objNew.set_dog_sound('bow bow')

print('the breed of {} is {} and it {}'.format(objNew.get_name(),objNew.get_breed(),objNew.get_dog_sound()))

print(str(objNew))

print(len(objNew))
		
print(objNew.get_color())




animal.specie = 'canine'

objNew2 = Dog('dog','black','doberman','No')

objNew2.set_dog_sound('bow bow')
print('the breed of {} is {} and it {}'.format(objNew2.get_name(),objNew2.get_breed(),objNew2.get_dog_sound()))
