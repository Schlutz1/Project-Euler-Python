#dank aff 

import math

#returns list, this is faster for iteration, but only slighter
def prime_generator(n) :
	sieve = [True] * (n+1)
	ps = []
	for p in range(2, n) :
		if sieve[p] :
			for i in range(p**2, n, p):
				sieve[i] = False
			ps.append(p)
	return ps


#this might be faster for lookup i.e. checking
def prime_generator_dictionary(n) :
	sieve = [True] * (n+1)
	ps = {}
	for p in range(2, n) :
		if sieve[p] :
			for i in range(p**2, n, p) :
				sieve[i] = False
			ps[p]=p
	return ps
