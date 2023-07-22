'''
def make_pizza(*toppings):
	print('\n making a pizza with following topics: ')
	for topping in toppings:
		print('-'+topping)
	#print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#mixing positional and arbitrary arguments
def pizza(size,*toppings):
	print('\n making a '+str(size)+'-inch with following toppings: ')
	for topping in toppings:
		print('-'+topping)
		
pizza(16,'pepperoni')
pizza(12,'mushrooms','green peppers','extra cheese')
#using arbitrary keyword argument

'''
def build_profile(first,last,**user_info):
#build a dictionary all you know about user	
	profile = {}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile
user_profile = build_profile('albirt','einstain',location='princeton',field='physics',job ='scientific')
#user_profile = build_profile(field='physics')
print(user_profile)





