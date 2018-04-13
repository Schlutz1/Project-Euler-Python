'''
q21 python implementation

'''

from functools import reduce


def find_proper_divisors(n):

	facSum = 0
	factors = set(reduce(list.__add__,
					  ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0))) #inds all factors

	for val in factors: #finds sum of factors
		facSum = facSum + val
	facSum = facSum - n 

	#print factors, facSum #disp vals
	return facSum #returns compare val


if __name__ == "__main__":

	amicableList = []
	aSum = 0

	for a in range(2, 10000) :
		compareVal = find_proper_divisors(a)

		if a == find_proper_divisors(compareVal) and a != compareVal: #evaluates if there is a match
			print a, compareVal
			amicableList.append(a)
			amicableList.append(compareVal)

	amicableList = set(amicableList)
	for value in amicableList:
		aSum = aSum + value

	print aSum