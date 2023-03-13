# Naive solution:
def NavCount(arr1):
    count = 0
    for i in arr1:
        if i == 1:
            count += 1
    if count == 0:
        return -1
    else:
        return count


arr1 = [0, 0, 0, 0, 1, 1, 1, 1]
print("The count is: ", NavCount(arr1))


# Optimized Approach
def first(arr):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] < 1:
            low = mid+1
        elif arr[mid] > 1:
            high = mid-1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid-1
    return -1


def last(arr):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] < 1:
            low = mid+1
        elif arr[mid] > 1:
            high = mid-1
        else:
            if mid == len(arr)-1 or arr[mid] != arr[mid+1]:
                return mid
            else:
                low = mid+1
    return -1


def OptimizedCount(arr):
    firstApp = first(arr)
    if first == -1:
        return 0
    else:
        return last(arr)-firstApp+1


arr = [0, 0, 0, 0, 1, 1, 1, 1]
print(OptimizedCount(arr))
