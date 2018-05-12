from decimal import Decimal
import re

#Attempt 2:

seqLen = 0

for i in range(100, 1, -1) :
	if seqLen >= i :
		break

	foundRemainders = [0]*i
	val = 1
	pos = 0

	while foundRemainders[val] == 0 and val != 0 :
		foundRemainders[val] = pos
		val *= 10
		val %= i 
		pos += 1


	if pos - foundRemainders[val] > seqLen :
		seqLen = pos - foundRemainders[val]

print "final ans: ", seqLen
'''
#Attempt 1, I suck at regex
def repetitions(s):
   r = re.compile(r"(.+?)\1+")
   for match in r.finditer(s):
       yield (match.group(1), len(match.group(0))/len(match.group(1)))

max_n, max_len = 0, 0
for n in range(1, 1000) :
	val = 10000000*(Decimal(1.0) / n)
	reps = list(repetitions(str(val)[2:]))
	#print "debug: ", n, val, reps
	for element in reps :
		repeat_len = len(str(element[0]))
		if repeat_len > max_len :
			max_len = repeat_len
			max_n = n
			print "new max: ", n, val, repeat_len, element[0]
'''