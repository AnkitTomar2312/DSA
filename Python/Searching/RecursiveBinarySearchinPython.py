def BSearch(arr,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==x:
        return True
    elif arr[mid]>x:
        return BSearch(arr,x,low,mid-1)
    else:
        return BSearch(arr,x,mid+1,high)
    
def Main(arr,x):
    return BSearch(arr,x,0,(len(arr)-1))


arr=[10,20,30,40,50,60,70]
x=80

print(Main(arr,x))


# Time complexity O(logn) recursive calls
# Auxiliary Space O(logn)