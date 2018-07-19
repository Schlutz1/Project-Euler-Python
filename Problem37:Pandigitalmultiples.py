# q37 python


from primeGenerator import prime_generator_dictionary


# execution for 100000 in 0.4s, 10000000 in 3s
# wrap c++ solution, faster execution?

prime_dict = prime_generator_dictionary(1000000)

running_total = 0
for k in prime_dict:

	ltr_bool, rtl_bool = False, False

	if k < 10 :
		continue 
	else :
		for counter, val in enumerate(str(k)):

			ltr = int(str(k)[counter:])
			x = int(len(str(k)) - counter)
			rtl = int(str(k)[:x])


			if rtl not in prime_dict :
				break

			if ltr not in prime_dict :
				break

			if counter == (len(str(k))-1) :
				print "prime trunk: ", k
				running_total += k
				print "running total: ", running_total



