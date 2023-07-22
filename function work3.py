#returning a dictionary
#returning a dictionary about a person

def build_person(first_name,last_name):
	person = {'first':first_name,'last':last_name}
	return person
musian = build_person('rabbi','hasan')
print(musian)


def build_person(first_name,last_name,age=''):
	if age:
		person['age'] = age
	return person
musian = build_person('rabbi','hasan',age=15)
print(musian)	
#using a function with while loop
def formatted_name(first_name,last_name):
	full_name = first_name+' '+last_name
	return full_name.title()

while True:
	print('\n')
	print('please tell me your name:')
	print('\n(enter Q at any time to quit)\n')
	f_name = input('first name:')
	if f_name == 'q':
		break
	l_name = input('last name:')
	if l_name == 'q':
		break
	formate = formatted_name(f_name,l_name)
	
	print('\nHello ' + formate + '!')

'''
#passing a list
def greet_user(names):
	# print a simple greeting of each user in the list
	for name in names:
		mgs = 'Hello '+ name.title() +'!\n'
		print(mgs)
		#print('Hello '+ name.title() +'!\n')
		if name=='':
			return name
			break
		
usernames = ['rabbi','ashik','sakib',]
system = greet_user(usernames)
print(system)
'''









