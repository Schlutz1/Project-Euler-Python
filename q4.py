import numbers

#problem 4, project euler


localMax = 0
localPal = 0

for i in range (317, 1000):
    for j in range(317, 1000):
        localPal = i * j
        if localMax < localPal:
            #print(localMax)
            strTrial = str(localPal)
            n = list(strTrial)
            if n[0][0] == n[5][0]:
                if n[1][0] == n[4][0]:
                    if n[2][0] == n[3][0]:
                        localMax = localPal

print(localMax)
