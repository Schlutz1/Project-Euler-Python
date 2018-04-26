#q20 factorial digits
# no significant differnces in methods

#import math
n = 100

'''
#boring mathod
# python q20.py  0.02s user 0.02s system 85% cpu 0.044 total
val = math.factorial(n)
print val
'''

#recursive method
#python q20.py  0.01s user 0.02s system 84% cpu 0.037 total
def factorial(n) :
	if n == 0 :
		return 1
	else :
		return n * factorial(n-1)

val = factorial(n)
_sum = 0
for digit in str(val) :
	_sum = _sum + int(digit)

print _sum

