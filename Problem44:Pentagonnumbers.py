#q44.py 

UPPER_LIMIT = 100000

import math

#checks if diff / sum is pentag
def is_pentag(n) :
	root = (0.5 + math.sqrt(0.5**2 + 4*1.5*n)) / (2 * 1.5)
	if int(root) == root :
		return True
	else :
		return False

#creates pentag numberss
def pentagonal_generator(n) :
	return (n*(3*n-1)/2)


for lhs in range(1, UPPER_LIMIT) :
	lhs_pent = pentagonal_generator(lhs)
	for rhs in range(lhs, UPPER_LIMIT) :
		rhs_pent = pentagonal_generator(rhs)
		if is_pentag(rhs_pent - lhs_pent) and is_pentag(rhs_pent + lhs_pent) :
			print lhs_pent, rhs_pent