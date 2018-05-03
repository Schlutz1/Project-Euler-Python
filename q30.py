#q30 python

#max val is 9^5 * 4 = 236196
#min val is 1^5 * 3 + 2^5 = 35

UPPER_LIMIT = 236196
#UPPER_LIMIT = 40
LOWER_LIMIT = 35


_sum = 0
for val in range(LOWER_LIMIT, UPPER_LIMIT) :
	val_counter = 0
	for vval in str(val) :
		val_counter += int(vval)**5
	if val_counter == val :
		print val
		_sum += val

print _sum