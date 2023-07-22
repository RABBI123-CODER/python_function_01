#storing a function in module
#import in a entier module
def make_pizza(size,*toppings):
	print('\nmaking a '+str(size)+' inch with the following toppings.')
	for topping in toppings:
		print('='+topping)
def make(size,*view):
	print(size)
	for x in view:
		print(':'+str(x))
#make(10,'rabbi','ashik','sakib')
#make_pizza(16,'mushrooms','green peppers','extra cheese')
