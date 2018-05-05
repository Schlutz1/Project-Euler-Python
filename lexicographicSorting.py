#creates a lexicographic sorting functionality
# string q = '3124', returns as ['1', '2', '3', '4']

# note can just use itertools, but wheres the education in that

import re

def stringSplitByNumbers(x):
    r = re.compile('(\d+)')
    l = r.split(x)
    return [int(y) if y.isdigit() else y for y in l]

def lexicographic_sorting(q) :
	return sorted(q, key = stringSplitByNumbers)

def next_lexicographic_permutation(q) :
	i = len(q) - 1
	while (i > 0 and q[i-1] >= q[i]) :
		i += -1

	if i <= 0 :
		return False

	j = len(q) - 1
	while (q[j] <= q[j-1]) :
		j += -1

	tmp = q[i-1]
	q[i-1] = q[j]
	q[j] = tmp

	j = len(q) - 1
	while (i < j) :
		tmp = q[i]
		q[i] = q[j]
		q[j] = tmp
		i, j = i+1, j-1

	print q
	return True
