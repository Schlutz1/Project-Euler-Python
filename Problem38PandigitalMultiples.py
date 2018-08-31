'''
Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def is_pandigital(num) :

	if len(num) != 9 :
		return False

	for n in range(1, 10) :
		if str(n) not in num :
			return False

	return True

def eval_num(x, n) :
	num_str = ""
	for _n in range(1, n+1) :
		num_str += (str(x * _n))
	return num_str


def generate() :
	
	for x in range(9999, 9000, -1) :
		num = eval_num(x, 2)
		if is_pandigital(num) :
			print(x, num)

if __name__ == "__main__" :
	
	generate()

	#num = eval_num(x, n)
	#if is_pandigital(num) :
	#	print(x, n, num)