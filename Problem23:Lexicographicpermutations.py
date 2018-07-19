#q23 python actual

import math

UPPER_LIMIT = 28123 

abun = []

#find if abundant number
def sumOfFactors(n, factors) :
	_sum = 0
	for val in factors :
		_sum += val
	if _sum > n :
		return True
	else :
		return False

#find all factors
def findProperDivisors(n):
	factors = [1]
	if n == 1:
		return 1
	_max = int(math.ceil((n ** 0.5)))
	for i in range(2, _max):
		if n % i == 0:
			factors.append(i) 
			factors.append(n/i)
	if (_max**2) == n:
		factors.append(_max)
	return factors

#find all abundant numbers
for i in range(2, UPPER_LIMIT) :
	if sumOfFactors(i, findProperDivisors(i)):
		abun.append(i)

abun2 = [True] * (UPPER_LIMIT+1)
for counter in range(len(abun)) :
	for ccounter in range(counter, len(abun)) :
		if (abun[counter] + abun[ccounter]) <= UPPER_LIMIT :
			abun2[abun[counter] + abun[ccounter]] = False
		else :
			break

_sum = 0
for n in range(UPPER_LIMIT) :
	if abun2[n] :
		_sum += n

print _sum