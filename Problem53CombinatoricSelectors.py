# problem53, combinatoric selectors
'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	(n! / r!(n−r)!)
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
'''

import numpy as np
import pandas as pd

def comb_generator(n, r) :
	n_factorial = np.math.factorial(n)
	r_factorial = np.math.factorial(r)
	nr_factorial = np.math.factorial(n-r)
	return (n_factorial / (r_factorial * nr_factorial))


if __name__ == "__main__" :

	n_max = 101
	thresh = 1000000
	

	counter = 0
	for n in range(1, n_max) :
		
		sub_counter = 0
		#even condition
		if n %2 == 0 :
			for r in range(int(n/2)+1) :
				val = comb_generator(n, r)
				if val > thresh :
					#print(n, r)
					#print(val)
					sub_counter += 1

			if sub_counter > 0 :
				inc = int(2*sub_counter - 1)
				#print("even inc: ", inc)
				counter += inc 
		
		#odd condition
		if n%2 == 1 :
			for r in range(int(n/2)+1) :
				val = comb_generator(n, r)
				if val > thresh :
					#print(n, r)
					#print(val)
					sub_counter += 1

			if sub_counter > 0:
				inc = int(2*sub_counter)
				#print("odd inc: ", inc)
				counter += inc 

	print("final counter: ", counter)
		

	# Pattern is symmetrical around n / 2
	# if even n, 1 <= r <= n / 2 (times count by 2, -1)
	# if odd n, 1 <= r <= n / 2 (times count by 2)

	'''
	# Code for visualising and outputting result for first 20 iterations
	c_list = []
	factor_list = []
	for n in range(n_max) :

		for r in range(n) :
			print("values: ", n, r)
			C = int(comb_generator(n, r))
			c_list.append(C)
			factors = str(n) + ", " + str(r)
			factor_list.append(factors)

	data = pd.DataFrame({'vals' : c_list})
	data['factors'] = factor_list
	data.to_csv("output.csv", index=True)
	'''
