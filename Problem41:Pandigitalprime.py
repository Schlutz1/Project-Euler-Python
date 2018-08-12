'''
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

#look at permutation of n-digit pandigitials

#start with n = 9, and look at all permutations not ending in an even number
#dec n until a prime is found 


def is_pandigital(q) :
	q = str(q)
	n = len(q)
	beg=set(q[0:n])
	end=set(q[-n:]) #checks if vals are 1 - n
	return beg==end and beg==set(map(str, range(1, n + 1))) #checks if each val is unique


from resource_primeGenerator import prime_generator

p_list = prime_generator(7654321)

for counter in range(len(p_list)-1, -1, -1) :
	val = p_list[counter]
	if is_pandigital(val) :
		print val
		break
