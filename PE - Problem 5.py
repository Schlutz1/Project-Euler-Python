# smallest multiple problem 5 PE

def isDivisible(x, y): #x = test value, y = number dividing i.e. 20%4 = 0
    if x%y == 0:
        return True
    else:
        return False

valueFound = False
counter = 0
rangeVal = 21

while valueFound == False:
    #print(counter)
    for i in range(1, rangeVal):
       dividedEvenly = isDivisible(counter, i)
       #print(i)
       if dividedEvenly == False:
            #print('Fail')
            break
       elif i == rangeVal-1:
            valueFound = True
            print('Lowest positive integer: ', counter)
    counter = counter+20

#this method could be substantially optimised - by iterating from 1 -> rangeVal, several unessecary function calls are made.
#the only divisions that matter are test/20, 19, 18, 17, 16, 15, 14, 13, 12, 11
#this occurs as any x < 10 is encapusalted in the above list i.e. for x = 7, as 14 is a multiple of 7, test/14 encapsulates test/7
