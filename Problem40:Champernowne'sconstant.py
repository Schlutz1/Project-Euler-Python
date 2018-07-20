#q40 python

spec = 13

decimal_place = 1
care = 1
for i in range(1, 1000000) :
	expansion = [int(i) for i in str(i)]
	for increment in expansion :

		if decimal_place == care :
			print decimal_place, increment
			care = care * 10

		decimal_place += len(str(increment))


