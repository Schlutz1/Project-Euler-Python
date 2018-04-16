# PE problem 7, 10001st prime

primeLimit = 500000 #arbitrary prime limit
sqPrimelimit = int(1000000**(.5)) #sufficently high enough factor list
boolPrimeArray = [True]*primeLimit
counter = 0

for i in range(2, sqPrimelimit+1): #derives array of primes
    if boolPrimeArray[i]==True:
            for j in range(i**2, primeLimit, i):
                boolPrimeArray[j] = False 

for y in range(3, primeLimit): #checks primes passed to boolPrimeArray
    if boolPrimeArray[y] == True:
            counter = counter + 1
            #print('prime: ', y)
            #print('counter: ', counter)
            if counter == 10000: #finds 10001 prime
                print(y)
