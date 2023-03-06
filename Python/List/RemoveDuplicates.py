print("Removing the Duplicates from the list: \n")

#Navive approach taking time O(n)

def RemoveDup(l,n):
    k=[0]*n
    k[0]=l[0]
    res=1
    for i in range(1,n):
        if k[res-1]!=l[i]:
            k[res]=l[i]
            res+=1
    for i in range(0,n):
        l[i]=k[i]
    print(l)
        



#Optimized Approach
def opti(l,n):
    res=1
    for i in range(1,n):
        if l[res-1]!=l[i]:
            l[res]=l[i]
            res+=1
    return(l)
l=[10,20,30,30,40,40,40,50]
n=len(l)
# RemoveDup(l,n)
print(opti(l,n))


