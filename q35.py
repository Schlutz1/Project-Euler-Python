#q35 python

from primeGenerator import prime_generator_dictionary

prime_dict = prime_generator_dictionary(1000000)


rt = 0
for key in prime_dict :

	for counter in range(len(str(key))) :
		tmp1 = str(key)[counter:]
		tmp2 = str(key)[:counter]

		val = int(tmp1 + tmp2)
		if val not in prime_dict :
			break
		if counter == len(str(key)) - 1 :
			rt += 1

print "total number: ", rt


	