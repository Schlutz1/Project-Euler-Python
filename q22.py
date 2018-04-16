'''
q22 python implementation
reqs: /QuestionFiles/p022_names.txt
'''

GLOBAL_CHAR_OFFSET = 64 #for ascii conversions

if __name__ == "__main__" :
	global GLOBAL_CHAR_OFFSET

	#file reading
	with open("./QuestionFiles/p022_names.txt") as file:
		x = [word for line in file for word in line.split(',')] #reads in contentx
	x_alpha = sorted(x) #sorts alphabetically
	print x_alpha

	#values for letters can be derived from ascii conversion
	# i.e. ord('a') = 97, ord('b') = 98,..., ord('z')=122
	# add offset of -96
	
	total_name_score = 0
	for counter, name in enumerate(x_alpha) :
		name_sum, name_score = 0, 0

		for letter in name:
			if letter == '"' :
				continue
			else :
				#print letter, ord(letter)
				name_sum = name_sum + (int(ord(letter)) - GLOBAL_CHAR_OFFSET) #calcs score for ecah letter
		
		name_score = name_sum * int(counter+1)
		print counter, name, name_score
		total_name_score = total_name_score + name_score

	print total_name_score
	