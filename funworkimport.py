'''
import funwork6
funwork6.make_pizza(12,'pepperony')
funwork6.make_pizza(16,'mushrooms','green peppers','extra cheese')

You can also import a specific function from a module.Here’s the general 
syntax for this approach:    ( from module_name import function_name  )
 
You can import as many functions as you want from a module by separating
 each function’s name with a comma:
( from module_name import function_0, function_1, function_2 )


from funwork6 import make_pizza
make_pizza(12,'pepperony')
make_pizza(16,'mushrooms','green peppers','extra cheese')

#using as to give a function an alias
from funwork6 import make_pizza as rabbi

rabbi(12,'pepperony')
rabbi(16,'mushrooms','green peppers','extra cheese')

#using as to give a module as alias
import funwork6 as f
f.make_pizza(12,'pepperony')
f.make_pizza(16,'mushrooms','green peppers','extra cheese')


#importing all function in a module
from funwork6 import*
make_pizza(12,'pepperony')
make_pizza(16,'mushrooms','green peppers','extra cheese')

#styling functions

def function_name(parameter_0, parameter_1, parameter_2,parameter_3, parameter_4, parameter_5):    
         function body...

'''
import funwork
funwork.build_profile('albirt','einstain',location='princeton',field='physics')
import funwork6
funwork6.make(10,'rabbi','ashik','sakib')
funwork6.make(100,'a','b','c')
funwork6.make_pizza(16,'mushrooms','green peppers','extra cheese')

print('\n')
print('\n')

from funwork6 import*
make(10,'rabbi','ashik','sakib')
make(100,'a','b','c')
make_pizza(16,'mushrooms','green peppers','extra cheese')

















