#q29 python
tmp = {}
for a in range (2, 101) :
	for b in range(2, 101) :
		val = a**b
		#print val
		tmp[val] = 1

counter = 0
for val in tmp :
	#print val
	counter += 1

print counter