# Naive Appraoch
def NavSquareRoot(x):
    i = 1
    while i*i <= x:
        i += 1
    return i-1


print(NavSquareRoot(15), "Time Complexity ==> O(sqareRoot(n)) \n")


# Optimised Approach
def OptiApp(x):
    low = 1
    high = x
    ans = -1
    while low < high:
        mid = (low+high)//2
        mSq = mid*mid
        if mSq == x:
            return mid
        elif mSq > x:
            high = mid-1
        else:
            low = mid+1
            ans = mid
    return mid


print(OptiApp(100), "Time Complexity ==> O(log N)")
