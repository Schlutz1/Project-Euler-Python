#problem 86, cuboid routes

import math
import sys

def shortest_path_integer(wh, l) :
	val = math.sqrt(wh*wh + l*l)
	if int(val) == val :
		return True 
	else :
		return False

if __name__ == "__main__" :


	integerPathCounter = 0
	l = 2
	target = 1000000

	while integerPathCounter < target : 
		l += 1

		for wh in range(3, (2*l)+1) :
			if shortest_path_integer(wh, l) :
				if wh <= l :
					integerPathCounter += wh / 2
				else :
					integerPathCounter +=  1 + (l - (wh+1)/2);
				

	print l

	'''
	top = 101
	for w in range(1, top) :
		for d in range(w, top) : 
			for h in range(d, top) :

				if shortest_path_integer(w, d, h) :
					integerPathCounter += 1

	print integerPathCounter

	'''