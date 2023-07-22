#function work
'''
def greet_user(user):
	print('hello ' + user.title())
greet_user('jesse')
greet_user('rabbi')

def pet(animal_type,animal_name):
	print('i have a ' + animal_type.title())
	print('my '+ animal_type.title() +' name is '+animal_name.title())
	print('\n')
pet('hamster','harry')
pet('dog','rocky')

#keyword arguments
pet('harry','hamster')
pet(animal_type = 'hamster',animal_name = 'harry')

#deafault values
def pets(animal_type = 'dog',animal_name = 'harry'):
	print('i have a ' + animal_type.title())
	print('my '+ animal_type.title() +' name is '+animal_name.title())
	print('\n')
pets()

pet(animal_name = 'harry',animal_type = 'hamster')
pets('dog')
pets(animal_name ='harry')


def make(size,meg):
	print('hello '+size.title())
make('everyone','welcome')
'''

def name(first_name,last_name):
	print('the first name '+first_name.title())
	print('the last name '+last_name.title())
	return name
	print('\n')
name('rabiul','hasan')
mem = name('size','meg')
print(mem)


def nam(first_name,middle_name,last_name):
	full_name = first_name+middle_name+last_name
	return full_name.title()
	#print('the last name '+last_name.title())
	print('\n')

wow = nam('ra','bb','i')
print(wow)
name('h','r')









