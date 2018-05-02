
'''
odcomp = some_prime + 2*n**2


take n
minus prime
see if val/2 has integer square root

^this solution requires continous checking aginst a list of primes
should this list be cached (best solution - memory issues?)
or done on the fly (slower?)
'''

from primeGenerator import prime_generator

prime_list = prime_generator(10000)

def rest_of_the_owl(n) :
	val = (n/2)**0.5
	if int(val) == val :
		return True
	else :
		return False


unfound = True
init_val = 1
while unfound :

	init_val += 2
	if init_val in prime_list :
		continue

	counter = 0
	unfound = False
	while init_val >= prime_list[counter] :
		if rest_of_the_owl(init_val - prime_list[counter]) :
			unfound = True
			break
		counter += 1
