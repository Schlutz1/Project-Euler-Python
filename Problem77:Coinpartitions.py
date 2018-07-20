#python 77 - prime summatiosn

from resource_primeGenerator import prime_generator

import sys

target = 2
prime_list = prime_generator(1000)
someBool = True

while someBool:
	ways = [0] * int(target+1)
	ways[0] = 1

	for i in range(len(prime_list)) :
		#i assigns the type of coin
		for j in range(prime_list[i], target+1) :
			#j iterates through the array
			#adds to based on position in array and val
			ways[j] += ways[j - prime_list[i]]
	print ways[target]
	if ways[target] > 5000 :
		print ways[target], target
		break
	target += 1
