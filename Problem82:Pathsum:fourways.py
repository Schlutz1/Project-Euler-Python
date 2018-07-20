#q82 path sum: three ways

'''
Test case 1

[1, 2, 3]
[4, 2, 1]
[5, 6, 2]

'''


def process_data() :
	with open("p081_matrix_test_test.txt") as file:
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

		print line 
		
		#for horiz_counter in range(len(line)) :
		#	continue