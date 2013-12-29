#Input: array A
#Output: max sum of non-empty subarray
#Goal: O(n) time

import random
def randomList(size,low=10,high=100):
    return map(lambda _:random.randint(low,high),xrange(size))

#Kadane's algorithm   
#without index version of Max-sum

def findMaxSum(arr):
    max_end_here = max_so_far = arr[0]
    for i in arr[1:]:
        max_end_here += i
        if max_end_here < i:
            max_end_here = i
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far        

#with index version of Min-Sum
def findMinSum(arr):
    min_end_here = min_so_far = arr[0]
    gl = gr = left = right = 0
    i = 1
    for x in arr[1:]:
        min_end_here += x
        right = i
        if min_end_here > x:
            min_end_here = x
            left = i
            
        if min_so_far > min_end_here:
            min_so_far = min_end_here
            gl = left
            gr = right
        i += 1
    return min_so_far, gl, gr

#Test
testArr = randomList(10, -10, 10)
print(testArr)
print(findMinSum(testArr))
