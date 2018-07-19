#q39 python implem

import operator

def valid_square(a, b, c) :
	if a**2 + b**2 == c**2 : 
		return True
	else :
		return False


if __name__ == "__main__" :

	soln_dict = {}

	for p in range(1, 1000) :
		print p
		a, b, base = p/3 - 1, p/3, p/3 + 1

		soln_counter = 0
		for counter, c in enumerate(range(base, p)) : #assigns c
			remainder = p - c
			for possible_vals in range(1, remainder/2) : #assigns a and b

				b = remainder - possible_vals
				a = possible_vals
				if valid_square(a, b, c) :
					print a, b, c
					soln_counter += 1

		soln_dict[p] = soln_counter


	print max(soln_dict.iteritems(), key=operator.itemgetter(1))[0]
					

	#find all tuples of values that add to p i.e. (n1, n2, n3), 

#disqualify all tuples that don't follow obvious convention of n3 > n2 >= n3

#check if square lengths 