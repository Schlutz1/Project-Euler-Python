# Problem 47 - Distinct Prime Factors
'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

from sympy.ntheory import factorint

if __name__ == "__main__" :

	# improved top down approach of generating values, and then finding prime factors

	notFound = True
	i = 1
	counter = 0
	depth = 4
	while notFound :
		factors = factorint(i)
		_len = len(factors)

		if _len == depth :
			counter += 1
			if counter == depth :
				print(i, i-(depth-1))
				notFound = False

		else :
			counter = 0


		i += 1


# stupid first attempt, tried to generate values based on prime factors (bottom up)
'''
	max = 20

	check_dict, agg_dict = {}, {}
	for i in range(max*max) :
		check_dict[i] = 0
		agg_dict[i] = 0

	prime_list = ret_primes1(max)

	depth = 2

	# two distinct factors
	for counter in range(len(prime_list)) :
		f1 = prime_list[counter]
		for f2 in prime_list[counter+1:] :		

			# evaluates n
			n = f1 * f2

			# check if already seen (not-distinct)
			if check_dict[n] < 1 :

				# does spooky aggregation stuff
				for i in range(depth) :
					if i == 0 :
						agg_dict[n] += 1

					else :
						agg_dict[n+i] += 1
						agg_dict[n-i] += 1

				if agg_dict[n] == depth :
					print(n)
					print(agg_dict)
					sys.exit()

			check_dict[n] = 1
'''