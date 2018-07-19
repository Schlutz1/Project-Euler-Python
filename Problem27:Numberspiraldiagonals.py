#q27 quadratic primes python - norm python

from resource_primeGenerator import prime_generator_dictionary


def quadraticPrimeGenerator(n, a, b) :
	return (n**2 + a*n + b)

def quadraticPrimeChecker(a, b, primeChecker) :

	#print "NEW SEQUENCE STARTING: ", a, b
	primeSequenceBool = True 
	n = 0
	while primeSequenceBool :
		val = quadraticPrimeGenerator(n, a, b)
		#print val
		if val not in primeChecker :
			return n
		else :
			n+=1


if __name__ == "__main__" :

	primeDict = prime_generator_dictionary(1000)
	primeChecker = prime_generator_dictionary(1000000)

	maxSeqLength = 0
	maxA, maxB = 0, 0
	top = 1000
	for b in primeDict : #b is neccessarily prime
		if b == 2 : #a is even if b == 2
			for  a in range(-top, top, 2) :
				seqLength = quadraticPrimeChecker(a, b, primeChecker) -1 #passes a, b comb to n chcker
				if seqLength > maxSeqLength :
					maxSeqLength = seqLength 
					maxA = a 
					maxB = b
					#print "New Max: ", maxSeqLength, maxA, maxB

		else : # else a is neccessarily odd
			for a in range(-top-1, top, 2) :
				seqLength = quadraticPrimeChecker(a, b, primeChecker) -1#passes a, b comb to n chcker
				if seqLength > maxSeqLength :
					maxSeqLength = seqLength 
					maxA = a 
					maxB = b
					#print "New Max: ", maxSeqLength, maxA, maxB

	print "Final Values", maxSeqLength, maxA, maxB
	print maxA * maxB