#problem 43: sub-string divisibility

'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the 
digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility 
property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

'''



#Notes: doesnt include original value, can't b be correct, look at n generator?

import time

import itertools
from itertools import compress
from itertools import permutations

def is_divisible(n) :

	string_length = 2
	prime_list = [2, 3, 5, 7, 11, 13, 17]
	# split into string, iterate over
	nl = [int(x) for x in str(n)]
	for counter in range(1, len(nl) - string_length) :

		# generate substrings
		sub_string = ''
		for i in range(string_length+1) :
			sub_string += str(nl[counter+i])
		
		if int(sub_string) % int(prime_list[counter-1]) != 0 :
			#print("broke here:", sub_string, prime_list[counter-1])
			return False

	return True


def next_pandigital_n() :
	# generate all pandigital numbers where the last 3 numbers are a multiple of 17


	n = 1406357289
	permutations = list(map("".join, itertools.permutations(str(n)))) # generate perms
	_set = set(permutations)
	result = list(_set)

	new_result = []
	for item in result :
		if int(item[7:]) % 17 == 0:
			new_result.append(item)

	print("Time start optimised")
	start = time.time()
	running_sum = 0
	for n in new_result:
		if is_divisible(n) :
			print("is a pandigital substring:", n)
			running_sum += int(n)
	end = time.time()
	print(end - start)

	print("Time start un-optimised")
	start= time.time()
	running_sum = 0
	for n in result:
		if is_divisible(n) :
			print("is a pandigital substring:", n)
			running_sum += int(n)
	end = time.time()
	print(end - start)

	return running_sum


if __name__ == "__main__" :

	running_sum = next_pandigital_n()
	print("total:", running_sum)
	'''
	n = 1406357289
	if is_divisible(n) :
		print("is a pandigital substring:", n)
	'''