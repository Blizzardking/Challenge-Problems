#Input: Array A of elemnts with values ranging from [1...n]
#Output: longest interval in array A
#Goal: Liner time

import random
def randomList(size,low=10,high=100):
    return map(lambda _:random.randint(low,high),xrange(size))

def getLargestInterval(li):
    s = set(li)
    inteval = 0
    mi = ma = li[0]
    for i in li:
        if i in s:
            s.remove(i)
            low = i -1
            while(low in s):
                s.remove(low)
                low -= 1
            high = i + 1
            while(high in s):
                s.remove(high)
                high += 1
            if(high - low > inteval):
                mi = low + 1
                ma = high - 1
                inteval = ma - mi
    return mi, ma

#Test
testList = randomList(10, 1, 10)
print(testList)
print(getLargestInterval(testList))
