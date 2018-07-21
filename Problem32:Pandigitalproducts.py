#q32 pandigital products - python

def test_values(a, b, c) :
	_string = str(a) + str(b) + str(c)

	if len(_string) != 9 : #checks flength for pandigitality
		return False

	for n in range(1, 10) : #checks for identity
		if str(n) not in _string :
			return False

	return True


def generate_values() :

	prodList = []
	_sum = 0

	'''
	this is the cool part
	
	rules :
	m*n = c
	len(m) + len(n) + len(c) = 10

	generating conditions:
	the only values that this is true for is

	len(m) = 1 and len(n) = 4
	or
	len(m) = 2 and len(n) = 3

	finally, the smallest possible value for n are all different values
	i.e. 123 or 1234

	bounds:
	2 <= m < 100
	123 <= n <= 10000 / m+1 for m < 10
	1234 <= n <= 10000 / m+1 for m > 10

	'''
	for m in range(2, 100) :
		if m > 9 :
			nStart = 123
		else :
			nStart = 1234

		nEnd = 10000 / (m+1)

		for n in range(nStart, nEnd) :
			c = m*n
			if test_values(m, n, c) :
				print m, n, c
				if c not in prodList :
					prodList.append(c)
				

	for c in prodList :
		_sum += c 

	print _sum




if __name__ == "__main__" :

	generate_values()