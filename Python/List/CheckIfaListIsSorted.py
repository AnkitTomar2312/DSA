print('This is program to check if the list is sorted: ')

def isSorted(l1):
    i=1
    while i<len(l1):
        if l1[i]<l1[i-1]:
            return False
        else:
            i+=1
    return True
print("using the While loop")
l1=[10,20,60,40,50]
print(isSorted(l1))


print('Using the sort method:')

def isSort(l2):
    sl = sorted(l2)
    if sl == l2:
        return True
    else:
        return False
    
l2=[10,20,30,80,50]
print(isSort(l2))