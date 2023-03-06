def averageOfList(l):
    sum=0
    for i in l:
        sum=sum+i
    n=len(l)
    return sum//n

l=[10,20,30,40,50,60,70]
print(averageOfList(l))



def avg(l):
    return sum(l)//len(l)

print(avg(l))