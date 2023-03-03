def getSmallerList(l,num):
    sl=[]
    for i in l:
        if(i<num):
            sl.append(i)
    return sl

l=[1,2,3,4,5,6,7,8,9,10]
num=7
print(getSmallerList(l,num))