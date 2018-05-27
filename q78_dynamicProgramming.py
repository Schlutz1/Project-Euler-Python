import sys

def p(n) :
	n+=1

	ways = [0] * n
	ways[0] = 1

	for i in range(1, n) :
		#i assigns the type of coin
		for j in range(i, n) :
			#j iterates through the array
			#adds to based on position in array and val
			ways[j] += ways[j - i]

	return ways[n-1]



if __name__ == "__main__" :
	#main things

	var = True
	n = 2
	while var :
		tmp = p(n)
		print n, tmp
		if tmp % 1000000 == 0 :
			print n, tmp
			sys.exit()
		n += 1