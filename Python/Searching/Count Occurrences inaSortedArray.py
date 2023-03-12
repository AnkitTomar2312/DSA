# Naive Approach
print("Naive Solution")


def NavCount(arr, x):
    count = 0
    for i in range(0, len(arr)-1):
        if arr[i] == x:
            count += 1
    return count


arr = [10, 20, 30, 40, 40, 40, 40, 40, 50, 60, 70]
x = 40
print(NavCount(arr, x), "TC ==> O(n)")


# Binary Search Solution
print("Binary Search solution")


def firstOcc(arr, x):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] > x:
            high = mid-1
        elif arr[mid] < x:
            low = mid+1
        else:
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid-1

    return -1


def lastOccu(arr, x):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low+high)//2
        if arr[mid] < x:
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            if mid == len(arr)-1 or arr[mid] != arr[mid+1]:
                return mid
            else:
                low = mid-1
    return -1


def findCount(arr, x):
    first = firstOcc(arr, x)
    if first == -1:
        return 0
    else:
        last = lastOccu(arr, x)
        return last-first+1


print(findCount(arr, x), "TC ==> O(log n)")
