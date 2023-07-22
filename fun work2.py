# making an argument optional

def name(f, m, l):
	full = f+ ' ' +m+ ' ' +l
	return full.title()
print('\n')
m = name('rabbi','rakib','robin')
print(m)
print('\n')
def nam(a,c,b=''):
	if b:
		full = a + ' ' + b + ' ' + c
	else:
		full = a + ' ' + c
	return full.title()	
n = nam('ashik','sakib','romjan')
print(n)
print(m)
print(n)
print('\n')
w = nam('ashik','romjan') 
print(w)
def num(a,c,b):
	if b=='':
		full = a + ' ' + b + ' ' + c
	else:
		full = a + ' ' + c
	return full.title()	
	
print('\n')	
	
q = num('ashik','rabbi','sakib')
print(q)	
	
	
	
