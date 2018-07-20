#q34 python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

running_total = -3
for n in range(10000000) :
	_sum = 0
	for element in str(n) :
		_sum += factorial(int(element))

	if _sum == n :
		print "match: ", n, _sum
		running_total += n
		print "running total: ", running_total