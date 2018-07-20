#q11 actual okay version

def hprod(matrix, y, x) :
	prod = 1
	for i in range(0, 4) :
		prod *= matrix[y][x+i]
	return prod

def vprod(matrix, y, x) :
	prod = 1
	for i in range(0, 4) :
		prod *= matrix[y+i][x]
	return prod

def ddiagonalprod(matrix, y, x) :
	prod = 1
	for i in range(0, 4) :
		prod *= matrix[y+i][x+i]
	return prod

def udiagonalprod(matrix, y, x) :
	prod = 1
	for i in range(0, 4) :
		try :
			prod *= matrix[y+i][x-i]
		except  :
			#one of those days
			return 0
	return prod

#main method
if __name__ == "__main__" :
	#read in file
	with open("p011_grid.txt") as file:
		x_line = [word for line in file for word in line.split(' ')]

	#auto adjust matrix dimensions for test cases
	dimension_counter = 1
	for val in x_line :
		if "\n" in val :
			dimension_counter += 1

	#init 20x20 matrix
	w, h = int(len(x_line) / dimension_counter), dimension_counter
	matrix = [[0 for x in range(w)] for y in range(h)] 

	#populate matrix
	x, y = 0, 0
	for val in x_line :
		if "\n" in val :
			val = val[:2]

		if x == int(len(x_line) / dimension_counter) :
			x = 0
			y += 1
		#print x, y, val
		matrix[y][x] = int(val)
		x += 1

	for line in matrix:
		print line

	#iterate through, pass each cell to prod methods, find max_prod
	max_prod = 1
	y = 0
	for line in matrix:

		x = 0
		for cell in line :

			#print matrix[y][x], cell
			if x + 3 >= w or y + 3 >= h :

				#up diagonal product condition
				prod = udiagonalprod(matrix, y, x)
				if prod > max_prod :
					max_prod = prod
					prod = 1

			else : 
				#horizontal product condition
				prod = hprod(matrix, y, x)
				if prod > max_prod :
					max_prod = prod
					prod = 1

				#vertical product condition
				prod = vprod(matrix, y, x)
				if prod > max_prod :
					max_prod = prod
					prod = 1

				#down diagonal product condition
				prod = ddiagonalprod(matrix, y, x)
				if prod > max_prod :
					max_prod = prod
					prod = 1

			x += 1

		y += 1
		
	print max_prod


