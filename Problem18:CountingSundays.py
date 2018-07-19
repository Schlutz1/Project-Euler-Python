#q18 - ;ath finding algos

# A* supposedly is best all round implementation for path finding algorithms?
# https://en.wikipedia.org/wiki/A*_search_algorithm

with open("problem_18.txt") as file:
	x_line = [word for line in file for word in line.split('\n')]

triangle = filter(None, x_line)
print triangle
nodes = []
for i in triangle:
	vals = i.split()
	nodes.append(vals)


max_row, prev_row = [], []
for row_counter, row in enumerate(nodes) :


	#prev_row, is previous row
	#max_row = max(row + prev_row)
	#prev_row = max_row

	if row_counter == 0:
		prev_row = row

	else :
		for elem_counter, element in enumerate(row) :

			#lhs
			if elem_counter == 0:
				val = int(element) + int(prev_row[elem_counter])
				max_row.append(val)
			#rhs
			elif elem_counter == len(row)-1:
				val = int(element) + int(prev_row[elem_counter-1])
				max_row.append(val)
			else :
				val1 = int(element) + int(prev_row[elem_counter-1])
				val2 = int(element) + int(prev_row[elem_counter])
				if val1 > val2 :
					max_row.append(val1)
				else :
					max_row.append(val2)

			#print max_row

		prev_row = max_row
		max_row = []

print max(prev_row)
