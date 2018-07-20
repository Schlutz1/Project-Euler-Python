#31 python - coin sums

'''
giving change to 5p using 1p and 2p
1, 1, 1, 1, 1
1, 1, 1, 2
1, 2, 2
'''


target = 201
coin_sizes = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * target
ways[0] = 1

for i in range(len(coin_sizes)) :
	#i assigns the type of coin
	for j in range(coin_sizes[i], target) :
		#j iterates through the array
		#adds to based on position in array and val
		ways[j] += ways[j - coin_sizes[i]]


print ways
