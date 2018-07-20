#q13 python implementation

with open("problem_13.txt") as file:
	x_line = [word for line in file for word in line.split(' ')] #reads in contentx

sum = 0	
for val in x_line :
	sum = sum + int(val)

print sum