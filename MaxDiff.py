#Maximum Difference between SubArrays from an Array
#Input : A[1.n]
#Output : Max Difference between .A[ij] and .A[kl](assume j < k here)
#Complexity : O(n)

#pseudocode
#Given Array A[1..N]
#Calculate Max[N] 
#- where Max[i]= max subarray in A[1..i] - O(N)
#Also store start and end indices in StartMax[N] and EndMax[N]
#Similarly Calculate Min[N] 
#- where Min[i] = min subarray in A[i+1..N]
#MinStart[N] and MinEnd[N] stores start and end indices for minimum subarray
#find the max difference between Max[i] and Min[i]
#
#Thus the total running time would be O(N).
#

import random
def randomList(size,low=10,high=100):
    return map(lambda _:random.randint(low,high),xrange(size))

#Adapt from Kadane's algorithm
#Assume that max-subarray on the left and min-subarray on the right;
#max-subarray on the right and min-subarray on the left are similiar, ommitted here
def maxDiff(arr):
    size = len(arr) 
    Max = [0 for i in xrange(size)]
    Min = [0 for i in xrange(size)]
    max_end_here = max_so_far = Max[0] = arr[0]
    i = 1
    for x in arr[1:]:
        max_end_here += x
        if max_end_here < x:
            max_end_here = x    
        max_so_far = max(max_so_far, max_end_here)
        Max[i] = max_so_far
        i += 1
    
    
    min_end_here = min_so_far = Min[size - 1] = arr[size - 1]
    i = size - 2
    for x in arr[size - 2::-1]:
        min_end_here += x
        if min_end_here > x:
            min_end_here = x
        min_so_far = min(min_so_far, min_end_here)
        Min[i] = min_so_far
        i -= 1
        
    maxDiff = Max[0] - Min[1]
    for i in xrange(size - 1):
        if(Max[i] - Min[i+1] > maxDiff):
            maxDiff = Max[i] - Min[i+1]
    return maxDiff, Max, Min
    


testArr = randomList(10, -10, 10)
print(testArr)
print(maxDiff(testArr))
                
                
            
