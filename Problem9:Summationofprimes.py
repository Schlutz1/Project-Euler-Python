# q9 triplets

p = 1000

a, b, base = p/3 - 1, p/3, p/3 + 1

soln_counter = 0
for counter, c in enumerate(range(base, p)):  # assigns c
	remainder = p - c
	for possible_vals in range(1, remainder/2):  # assigns a and b

		b = remainder - possible_vals
		a = possible_vals
		lhs, rhs = a**2 + b**2, c**2
		if lhs == rhs :
			print a, b, c
			print a*b*c

