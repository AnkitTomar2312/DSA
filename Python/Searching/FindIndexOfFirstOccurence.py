# Naive Approach
print("Naive Appraoch: \n")


def findIndexOf(arr, x):
    for i in range(0, len(arr)-1):
        if arr[i] == x:
            return i


arr = [10, 20, 30, 40, 50, 60, 70]
x = 40
print(findIndexOf(arr, x), '\n')

print("Recursive Appraoch: \n")

# Optimized approach


def firstOccurence(arr, x, low=0, high=len(arr)-1):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] > x:
        return firstOccurence(arr, x, low, arr[mid-1])
    elif arr[mid] < x:
        return firstOccurence(arr, x, arr[mid+1], high)
    else:
        if mid == 0 or arr[mid-1] != arr[mid]:
            return mid
        else:
            return firstOccurence(arr, x, low, arr[mid-1])


print(firstOccurence(arr, x),
      'Time Complexity is => O(log n), Aux Space=> O(log n) \n')


print("Iterative Approach \n")


def IterativeApp(n, x):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] < x:
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid-1
    return -1


print(IterativeApp(arr, x), 'Time Complexity is => O(log n), Aux Space=>theta(1) \n')
