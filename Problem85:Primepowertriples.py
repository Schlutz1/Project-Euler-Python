#q85 counting rectangles

#initalise width at max, and length at min
WIDTH = 2000
LENGTH = 1


def eval_rects(m, n) :
	'''
	gives no rects for some m x n grid where m > n

	3*2
	2*2
	1*2
	3*1
	2*1
	1*1

	f(2, 2) = 9
	f(3, 2) = 18
	f(3, 3) = 36

	for some m x n rect where m > n

	no_squares = m(m+1)n(+1)/4
	'''
	return (m*(m+1)*n*(n+1))/4



#progammatic evaluation, could probably derive inverse eqn but nah

for w in range(WIDTH, 1, -1) :
	if w < WIDTH ** 0.5 :
		break
	for l in range(LENGTH, WIDTH, 1) :
		val = eval_rects(w, l)
		#print w, l, val
		if val <= 2001000 and val >= 1999000 : #in range continue increment l till outside
			print w, l, val
		elif val >= 2001000 :
			break
		elif val <= 1999000 :
			l += 1


