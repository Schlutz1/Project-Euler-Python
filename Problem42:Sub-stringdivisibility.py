#q42 python

import math

#tests if triag
def is_triag(n) :
	root = (-0.5 + math.sqrt(0.5**2 + 4*0.5*n)) / (2 * 0.5)
	if int(root) == root :
		return True
	else :
		return False

#gets ascii val
def ascii_val(letter) :
	if letter == "\"" :
		return 0
	else :
		return (int(ord(letter)) - 64) 

with open("p042_words.txt") as file:
	x_line = [word for line in file for word in line.split('","')] #reads in contentx

counter = 0
for word in x_line :
	word_sum = 0
	for letter in word :
		word_sum += ascii_val(letter)
	if is_triag(word_sum) :
		counter += 1

print counter



