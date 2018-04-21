# q33 python implementatin - Digit Cancelling Fractions

# init num / denom = 11 / 12

from __future__ import division

MAX_VAL = 100
global prod_num, prod_denom

# iteration step


def iter_fraction(_num, _denom):
	for denom in range(_denom, MAX_VAL):
		if denom % 10 == 0:
			continue
		else:  # this part creates the valid denoms
			for num in range(_num, denom):
				eval_fraction(num, denom)
	# iteration through denom loop
		# iterate through num loop
			# if num bigger than denom, brea
			# else eval_frac
	return 0

# evaluation step


def eval_fraction(num, denom):
    if any(bit in str(num) for bit in str(denom)): #indicates a match condition
        og_frac = float(num / denom)
        common_val = list(set(str(num)).intersection(str(denom)))
        common_val =  str(common_val[0])

        if str(num)[0] == common_val :
        	_num = str(num)[1]
        else :
        	_num = str(num)[0]

        if str(denom)[0] == common_val :
        	_denom = str(denom)[1]
        else :
        	_denom = str(denom)[0]

        #_num, _denom = str(num).strip(common_val), str(denom).strip(common_val)
       
       	# print num, denom, _num, _denom

       	# removes too many values! i.e. 33 / 63 -> none / 6

       	new_age_frac = int(_num) / int(_denom)
       	# print og_frac, new_age_frac
       	if og_frac == new_age_frac :
       		print num, denom, _num, _denom, og_frac, new_age_frac
       		#prod_num, prod_denom = prod_num * _num, prod_denom * _denom
       		#print prod_num, prod_denom

    return 0


if __name__ == "__main__":

	_num, _denom = 11, 12
	iter_fraction(_num, _denom)
    # eval_fraction(num, denom)
