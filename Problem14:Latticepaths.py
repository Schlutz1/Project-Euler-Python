#q14 project euler - collatz

c_map = {}
def collatz_sequence(n) :
	if n in c_map:
		return c_map[n]
	if n % 2 == 0:
		 x = 1 + collatz_sequence(int(n/2))
	else:
		x = 1 + collatz_sequence(int(3*n+1))
	c_map[n] = x
	return x



largest_so_far = 1
highest = 0
for i in range(1,1000000):
    temp = collatz_sequence(i)
    if temp > largest_so_far:
        highest = i
        largest_so_far = temp


print largest_so_far