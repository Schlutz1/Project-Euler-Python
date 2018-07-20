#q81 python

def process_data() :
	with open("p081_matrix.txt") as file:
		x_line = [word for line in file for word in line.split(',')]
	matrix_lines = [l.split(',') for l in ','.join(x_line).split('\n')]
	return matrix_lines

if __name__ == "__main__" :

	matrix_lines = process_data()
	matrix = [0]*len(matrix_lines[0])
	prev_line = []

	for vert_counter, line in enumerate(matrix_lines) :
		horiz_counter = 0
		line = filter(None, line) #removes any whitespace
		line = [int(i) for i in line]

		#print prev_line, line

		
		for horiz_counter, element in enumerate(line) :

			#covers first horiz condition
			if vert_counter == 0 and horiz_counter != 0: 
				line[horiz_counter] += line[horiz_counter - 1] 

			#covers the vertical condition
			if vert_counter != 0 and horiz_counter == 0 :
				line[horiz_counter] += prev_line[horiz_counter]
			
			#rest of lines
			if vert_counter != 0 and horiz_counter != 0 :
				l_val = line[horiz_counter - 1]
				t_val = prev_line[horiz_counter]

				#print "lval, tval, init", l_val, t_val, line[horiz_counter]

				if l_val < t_val :
					line[horiz_counter] += l_val
				else :
					line[horiz_counter] += t_val

				#print "lval, tval, result", l_val, t_val, line[horiz_counter]

		prev_line = line
		print line
		



	'''
	for value :
				if first row, add to val to right, add to val directly below
				else 
					if value to left is smaller add, fi value above is smaller add
					prop down
					find smallest val
	'''

