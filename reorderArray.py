import random
def randomList(size,low=10,high=100):
    return map(lambda _:random.randint(low,high),xrange(size))

def reorder(arr):
    def _reorderHelper(arr, i, j):
        mid = (i + j)/2;
        if i >= j:
            return
        _reorderHelper(arr, i, mid)
        _reorderHelper(arr, mid + 1, j)
        plusBegin = i
        while plusBegin <= mid and arr[plusBegin] < 0: 
            plusBegin += 1
        negEnd = mid + 1
        while negEnd <= j and arr[negEnd] < 0: 
            negEnd += 1
        negEnd -= 1
        flipover(arr, plusBegin, mid)
        flipover(arr, mid + 1, negEnd)
        flipover(arr, plusBegin, negEnd)
        
    def flipover(arr, i, j):
        while(i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    _reorderHelper(arr, 0, len(arr) -1)
    return arr
    
#Test
arr = randomList(100, -10, 10)
print arr 
reorder(arr)
print arr 
   
