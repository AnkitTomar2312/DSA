print("Left Rotating the list by One")


#using direct library methods

#Using the slicing method
l=[10,20,30,40,50]
n=len(l)
l=l[1:]+l[0:1]
print(l)

#Using the Append method
l.append(l.pop(0))
print(l)


#using Our own method:

def RotateByOne(l,n):
    x=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=x
    print(l)

RotateByOne(l,n)