#q25 python

import sys

FuckAccenture = True

counter = 3

nmin1, n = 1, 1
while FuckAccenture :

	tmp = n
	n += nmin1
	nmin1 = tmp

	val = str(n)
	val = len(val)
	if val == 1000 :
		print counter, val
		sys.exit()

	counter += 1




