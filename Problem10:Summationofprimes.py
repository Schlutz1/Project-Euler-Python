#q10 prime summation

from primesieve.numpy import *

range = 2000000

prime_array = primes(range)

sum = 0
for element in prime_array :
	sum = sum + element

print sum