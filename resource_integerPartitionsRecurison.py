#python 31 coin sums

q = { 1: [[1]] }

def generate_partitions(n) :
    try :
        return q[n]
    except :
        pass

    result = [[n]]

    coin_list = [1, 2, 5, 10]
    #for i in coin_list:
    for i in range(1, n) :
        a = n-i
        R = generate_partitions(i)
        for r in R:
            if r[0] <= a:
                result.append([a] + r)

    q[n] = result
    return result

res =  generate_partitions(100)
print len(res)-1