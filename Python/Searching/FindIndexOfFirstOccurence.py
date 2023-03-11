# Naive Approach
def findIndexOf(arr,x):
    for i in range(0,len(arr)-1):
        if arr[i]==x:
            return i
        
arr=[10,20,30,40,50,60,70]
x=40
print(findIndexOf(arr,x))


#Optimized approach

