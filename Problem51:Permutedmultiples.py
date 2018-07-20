#q51 python - prime digit replacements

from primesieve.numpy import *

def find_prime_families(prime_list) :
	pf_dict = {}
	fam_len = str(prime_list[0])
	for possible_digit in range(1, 10) : #iterate from 1 to 10, checking vals
		print possible_digit


	return 0




if __name__ == "__main__" :
	range = 100
	prime_list = primes(10, range)

	find_prime_families(prime_list)