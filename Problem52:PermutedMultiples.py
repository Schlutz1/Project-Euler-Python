#Problem 52 - Permuted Multiples

'''
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, 
such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

from __future__ import division
import sys

def is_permuted_multiple(x) :

	prev_perm = sorted(map(int, str(x*1)))
	for multiple in range(1, 7) :
		perm  = sorted(map(int, str(x*multiple)))
		if perm != prev_perm :
			return False
		prev_perm = perm

	return True

def generate_x() :
	
	factor = 1
	no_match = True
	while no_match :

		lower_bound = 10**factor
		upper_bound_max = 10**(factor+1)
		upper_bound = upper_bound_max / 6

		for x in range(lower_bound, int(upper_bound)+1) :
			if is_permuted_multiple(x) :
				print x
				sys.exit()

		factor += 1


if __name__ == "__main__" :
	
	generate_x()
	



