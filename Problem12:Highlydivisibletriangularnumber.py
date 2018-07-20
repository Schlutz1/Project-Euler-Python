#q12 python

import sys
import math

'''
#removed this as recursion in python sucks massively
#refactor meomisation
m_map = {}
def triangle_number_generator(n) :
	if n in m_map :
		return m_map[n]
	if n == 0 :
		return 0
	else :
		x =  n + triangle_number_generator(n-1)
	m_map[n] = x
	return x
'''


#this solution is better anyway
val = 0
def triangle_number_generator(n) :
	global val

	val = n + val
	return val

if __name__ == "__main__" :

	insuff_div = True
	n = 0

	while insuff_div:
		n+=1
		t_number =  triangle_number_generator(n)
		div_list = []

		top = int(math.ceil(t_number ** 0.5))

		for i in range(1, top) :
			if t_number % i == 0 :
				div_list.append(i)
				div_list.append(t_number / i)

		#print n, t_number, div_counter
		if len(div_list) > 500 :
			print n, t_number, div_list
			sys.exit()