print("Reversing the list using different Library methods: \n")

print("It uses .reverse() method \n")
l0=[10,20,30,40,50]
l0.reverse()
print(l0)
print('\n')

print("It uses .list(reversed()) method \n")
l1=[10,20,30,40,50]
l2=list(reversed(l1))
print(l2)
print('\n')

print("It uses l1[::-1] method \n")
l3=[10,20,30,40,50]
l4=l1[::-1]
print(l2)
print('\n')



print('Our Own Method to reverse a list: \n')

def OwnReverse(l):
    s=0
    d=len(l)-1
    while s<d:
        l[s],l[d]=l[d],l[s]
        s+=1
        d-=1
    return l
l=[10,20,30,40,50]
print(OwnReverse(l))