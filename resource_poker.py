'''
resource_poker.py: poker hand evaluation file

'''

import math

# allocates score to intravalue poker hands i.e. same types
# return some value from 0 <= val <= 1000000, to give micro bounds


def intravalue_rank(interValueScore, histogram_dict, num_list, suit_list):
	val = 0
	counter = 0

	#highest card value
	if interValueScore == 0:
		for counter in range(len(num_list)):
			# weight higher cards more
			val += math.pow(14, counter)*num_list[counter]
		return int(val)

	#one pair
	if interValueScore == 1000000 :
		for key, value in sorted(histogram_dict.iteritems(), key=lambda (k, v): (v, k), reverse=True):
			val += math.pow(14, 3-counter)*int(key)
			counter += 1
		return int(val)

	#two pair
	if interValueScore == 2000000 :
		for key, value in sorted(histogram_dict.iteritems(), key=lambda (k, v): (v, k), reverse=True):
			val += math.pow(14, 2-counter)*int(key)
			counter += 1
		return int(val)

	#three of a kind
	if interValueScore == 3000000 :
		return num_list[2]

	#straight
	if interValueScore == 4000000 :
		for counter in range(len(num_list)):
			# weight higher cards more
			val += math.pow(14, counter)*num_list[counter]
		return int(val)

	#flush
	if interValueScore == 5000000 :
		for counter in range(len(num_list)):
			# weight higher cards more
			val += math.pow(14, counter)*num_list[counter]
		return int(val)

	#full house
	if interValueScore == 6000000 :
		return num_list[2]

	#four of a kind
	if interValueScore == 7000000 :
		return num_list[0]

	#straight flush
	if interValueScore == 8000000 :
		for counter in range(len(num_list)):
			# weight higher cards more
			val += math.pow(14, counter)*num_list[counter]
		return int(val)

# allocates score to intervalue poker hands i.e. different types
# return some value of 0 <= val <= 8000000 to give macro bounds


def intervalue_rank(histogram, isFlush, isStraight):

	#print "hist:", histogram
	if isStraight and isFlush:
		#print "straight flush"
		return 8000000
	if histogram[0] == 4:
		#print "four of a kind"
		return 7000000
	if histogram[0] == 3 and histogram[1] == 2:
		#print "full house"
		return 6000000
	if isFlush:
		#print "flush"
		return 5000000
	if isStraight:
		#print "straight"
		return 4000000
	if histogram[0] == 3 and histogram[1] == histogram[2]:
		#print "three of a kind"
		return 3000000
	if histogram[0] == 2 and histogram[1] == 2:
		#print "two of a kind"
		return 2000000
	if histogram[0] == 2 and histogram[1] == 1:
		#print "1 pair"
		return 1000000
	else:
		#print "high card"
		return 0#


def is_flush(suit_list):

	# looks for flushes n shit
	for counter in range(len(suit_list)-1):
		if suit_list[counter] != suit_list[counter+1]:
			# print "not flush"
			return False
	return True##


def is_straight(num_list, histogram):

	dif = num_list[4] - num_list[0]
	# if range of 4, and 5 unique cards, is straight
	if dif == 4 and len(histogram) == 5:
		return True
	else:
		return False


def card_ranks(num_list):

	# looks for pairs n shit
	histogram = {}
	for val in num_list:
		# increments existing
		if val in histogram.keys():
			histogram[val] = histogram[val]+1

		# inits histogram
		if val not in histogram.keys():
			histogram[val] = 1

	return histogram.values(), histogram

'''
# ================================================#
#                  SECTION BREAK                  #
# ================================================#

- MAIN method to be called from external files
- evalutes intra and interrank values for poker hands
- normalises royal cards for numeric evaluation
'''

def hand_analysis(hand):  # guts of hand compariosn

	num_list, suit_list = [], []

	for counter, val in enumerate(hand):  # breaks list into components
		if counter % 3 == 0:
			if val == "T":
				val = "10"
			if val == "J":
				val = "11"
			if val == "Q":
				val = "12"
			if val == "K":
				val = "13"
			if val == "A":
				val = "14"
			num_list.append(int(val))
		if (counter - 1) % 3 == 0:
			suit_list.append(val)

	num_list = sorted(num_list)  # sorts for further iteration

	#print hand

	#evals state of hand
	histogram, histogram_dict = card_ranks(num_list)
	histogram = sorted(histogram, reverse=True)
	isFlush = is_flush(suit_list)
	isStraight = is_straight(num_list, histogram)

	#find inter and intrarank values from hands
	interValueScore = intervalue_rank(histogram, isFlush, isStraight)
	intraValueScore = intravalue_rank(
		interValueScore, histogram_dict, num_list, suit_list)

	#print "ranks", histogram, "flush:", isFlush, "straight:", isStraight
	#print "inter: ", interValueScore
	#print "intra: ", intraValueScore

	return interValueScore + intraValueScore
