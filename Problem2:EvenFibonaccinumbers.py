from multiprocessing import Pool

rt = 0

def f(x) :
	global rt
	if x%3 == 0 or x%5 == 0:
		rt += x

	return 0

if __name__ == "__main__" :
	n = range(1, 10)
	p = Pool(2)
	p.map(f, n)
