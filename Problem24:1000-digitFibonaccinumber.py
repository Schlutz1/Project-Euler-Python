#q24 python
import itertools, sys


q = '0123456789'

temp = itertools.islice(itertools.permutations(q), 999999, None)
print "".join(str(x) for x in next(temp))

