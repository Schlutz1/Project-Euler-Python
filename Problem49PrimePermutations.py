# problem 49 - Prime Permutations

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import itertools
from itertools import compress
from itertools import permutations
from operator import eq

def ret_primes1(n):
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1,int(n**0.5)//2+1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]






def same_difference(prime_array) :
	prime_array = sorted(prime_array)
	#print(prime_array)
	diff_array = []
	for counter in range(len(prime_array) -1) :
		diff_array.append(prime_array[counter+1] - prime_array[counter])
	if len(diff_array) != len( list(set(diff_array)) ) : #check for values w same difference
		
		for counter in range(len(diff_array)-1 ) :
			if diff_array[counter] == diff_array[counter+1] :
				print(diff_array[counter], diff_array[counter+1])
				

				print(prime_array)
				print(diff_array)
				print(list(set(diff_array)))
				return True
				
	else :
		return False
		#print("no match")
		#print(len(diff_array), len( list(set(diff_array))))
		





if __name__ == "__main__" :
	primes = ret_primes1(10000)
	#d_primes = collections.OrderedDict()
	#print(len(primes))
	d_primes = {}
	for prime in primes :
		if prime >= 1000 and prime < 10000 :
			d_primes[prime] = False

	#print(len(d_primes))
	# iterate over keys, if prime perm, change to true
	for key, value in d_primes.items() : #generate primes
		if value == False:
			permutations = list(map("".join, itertools.permutations(str(key)))) # generate perms

			_set = set(permutations)
			result = list(_set)
			
			valid_prime_perms = [] #check if a sufficent number of perms are prime
			for perm in result :
				if int(perm) in d_primes :
					valid_prime_perms.append(int(perm))

			# create array of prime permutations
			if len(valid_prime_perms) > 2 :

				if same_difference(valid_prime_perms):
					print("FINAL PRIME ARRAY: ", valid_prime_perms)
					break

				# sets prime perms to true to avoid duplicate searching
				for valid_prime in valid_prime_perms :
					d_primes[valid_prime] = True



		#if key > 1030 :
			#break

					# NOTE: IF A PRIME HAS NO PERMUTATIONS THAT ARE TRUE, SET IT TO BEING FALSE
					# PUT A COUNTER, IF COUNTER 0, KEY IS USED TO SET FALSE IN DICT

	#d_primes = { k:v for k, v in d_primes.items() if v }

		


