def make_pizza(*toppings):
	print("\n making a pizza by using following::")
	for topping in toppings:
		print('-'+' '+topping)

make_pizza('peperony')
make_pizza('mushrooms','green peppers','extra cheese')
