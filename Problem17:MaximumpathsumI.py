#q17 python

import n2w

letter_counter = 0
for i in range(1000) :
    name = n2w.convert(i)
    name = name.replace(" ", "")
    letter_counter+=len(name)

    if i % 100 != 0 :
        letter_counter += 3

print letter_counter