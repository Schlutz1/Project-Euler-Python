#q45 

import math

def hex_generator(n) :
	return n*(2*n-1)

def is_pentag(n) :
	root = (0.5 + math.sqrt(0.5**2 + 4*1.5*n)) / (2 * 1.5)
	if int(root) == root :
		return True
	else :
		return False

def is_triag(n) :
	root = (-0.5 + math.sqrt(0.5**2 + 4*0.5*n)) / (2 * 0.5)
	if int(root) == root :
		return True
	else :
		return False

notFound = True
n = 2
while notFound :
	val = hex_generator(n)
	if is_pentag(val) and is_triag(val) and n!=143:
		print val
		notFound = False
	n+=1