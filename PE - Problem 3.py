import numbers

# prime factors Q3 PE

test = 600851475143

primeLimit = 10000
sqPrimelimit = int(50**(.5))
boolPrimeArray = [True]*primeLimit

for i in range(2, sqPrimelimit+1):
    if boolPrimeArray[i]==True:
            for j in range(i**2, primeLimit, i):
                boolPrimeArray[j] = False

#for y in range(3, primeLimit): #checks primes passed to boolPrimeArray
    #if boolPrimeArray[y] == True:
        #print(y)

for k in range(3, len(boolPrimeArray)): #checks to find factors of test in regards to boolPrimeArray
    if boolPrimeArray[k] == True:
        if test%k == 0:
            print(k)
