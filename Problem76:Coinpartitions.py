#python 76 - counting summations

target = 101
#coin_sizes = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * target
ways[0] = 1

for i in range(1, target) :
	#i assigns the type of coin
	for j in range(i, target) :
		#j iterates through the array
		#adds to based on position in array and val
		ways[j] += ways[j - i]

print ways[target-1]-1