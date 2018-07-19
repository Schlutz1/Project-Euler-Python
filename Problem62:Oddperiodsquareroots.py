#cubic permutations - python

''''
are 1001 and 0011 valid permuations?
how about 1001 and 11?
changes the answer substantially, and is not suitable to brute force otherwise

'''

import itertools
import sys

def is_cube(n) :
	c = int(n**(1/3.))
	return (c**3 == n) or ((c+1)**3 == n)

bool = True
val = 345

var_list = []
while bool :

	var_list = []
	cube = val**3

	#print "RESET, VAL:" , val

	for value in list(itertools.permutations(str(cube))) :
		var = int(''.join(value))
		if is_cube(var) and var not in var_list:
			var_list.append(var)
			#print var, var**(1/3.), len(var_list)

			if len(var_list) > 4 :
				print val
				print var_list
				sys.exit()

	#end of permuatation
	#increment val, reset bool array
	val+=1
