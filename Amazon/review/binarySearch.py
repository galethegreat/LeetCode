def binSearch(array, target, low, high):
    if low > high: return False
    midpoint = low + (high - low) // 2
    if array[midpoint] == target:return midpoint
    elif array[midpoint] > target:
        high = midpoint - 1
        return binSearch(array, target, low, high)
    elif array[midpoint] < target:
        low = midpoint + 1
        return binSearch(array, target, low, high)
    return -1


n = [1,5,12,13]
target = 0
print(binSearch(n,target,0,len(n)-1))
