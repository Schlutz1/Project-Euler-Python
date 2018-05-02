#dank aff 

import math

def prime_generator(n) :
	sieve = [True] * (n+1)
	ps = []
	for p in range(2, n) :
		if sieve[p] :
			for i in range(p**2, n, p):
				sieve[i] = False
			ps.append(p)
	return ps
