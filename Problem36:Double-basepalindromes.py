#q36 python

def is_bin_pallindrome(n) :
	bin_rep = "{0:b}".format(n)

	_len = len(str(bin_rep))
	
	for counter in range(_len) :
		if str(bin_rep)[counter] != str(bin_rep)[_len-counter-1] :
			break

		if counter == _len-1  :
			print bin_rep
			return True

rt = 0
for n in range(1, 1000000) :
	_len = len(str(n))
	
	for counter in range(_len) :
		if str(n)[counter] != str(n)[_len-counter-1] :
			break

		if counter == _len-1  and is_bin_pallindrome(n):
			rt += n
			print n

print rt

