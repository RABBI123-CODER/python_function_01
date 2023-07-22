#modifying a list in a function
'''
#start with some design that need to be a printed

unprinted_designs = ['iphone case','robot pedant','dodecahedron']

completed_models = []
#current_designs = unprinted_designs.pop()
#print(current_designs)
#simulate printing each devices, until none are left
#move each designs to completed_designs after printing
while unprinted_designs:
	current_designs = unprinted_designs.pop()
	#print(current_designs)
#simulate creating a 3d print from the device
	print('printing model:'+current_designs)
	completed_models.append(current_designs)
#display all complete models	
print('\nthe following models are printed:')	
for complete_model in completed_models:
	print(complete_model)
'''
#in the above code written in function

def print_models(unprinted_designs,complete_design):
	while unprinted_designs:
		current_designs = unprinted_designs.pop()
		#print(current_designs)
		print('printing model: '+current_designs)
		completed_models.append(current_designs)   # assign current_design data into complete_models
	
	
def show_completed_models(completed_models):
	print('\nthe following models are printed:')
	for complete_model in completed_models:
		print(complete_model)
		
		
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)   #this is call function to function copy

#print_models(unprinted_design,completed_models)

show_completed_models(completed_models)

#print(mgs1)
#print(mgs2)
#this function is very useful of every moment
'''
This example also demonstrates the idea that 
every function should have one specific job. 
The first function prints each design, 
and the second displays the completed models. 
This is more beneficial than using one function to do both jobs. 
'''










