#q50 python

from primeGenerator import prime_generator


UPPER_LIMIT = 1000000

prime_list = prime_generator(UPPER_LIMIT)


#Attempt 1:
max_len, max_val = 2, 0
for val in prime_list :
	#print "init val: ", val

	len_counter = 1
	for vval in prime_list[val-1:] :

		val += vval

		if val >= UPPER_LIMIT :
			break

		#print "+val, result, len: ", vval, val, len_counter
		len_counter += 1

		if val in prime_list :

			if len_counter > max_len :
				max_len = len_counter
				max_val = val
				print "max vals: ", max_len, max_val
