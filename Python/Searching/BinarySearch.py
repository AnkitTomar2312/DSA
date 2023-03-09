def BinSearch(n,x):
    low=0
    high=len(n)-1
    while low<=high:
        mid=(low+high)//2
        if n[mid]==x:
           
            return True
        elif n[mid]<x:
            low=mid+1
           
        else:
            high=mid-1
            
    return -1



n=[10,20,30,40,50,60]
x=10
print(BinSearch(n,x))