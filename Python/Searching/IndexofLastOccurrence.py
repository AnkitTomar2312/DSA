# Naive Approach
def navApp(arr, x):
    for i in reversed(range(len(arr))):
        if arr[i] == x:
            return i
    else:
        return -1


arr = [10, 20, 30, 40, 40, 40, 40, 50, 60, 60, 70]
x = 40

print("Last Occurence:", navApp(arr, x), "TC==>O(log n)")

# Iterative Approach:


def RecApp(n, x, low=0, high=len(arr)-1):
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
                low = mid+1
    return -1


print(RecApp(arr, x), "Tc==>O(log n), Aux Space ==> theta(1)")
