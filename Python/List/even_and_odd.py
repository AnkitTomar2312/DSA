def evenOdd(l):
    evenList=[]
    oddList=[]
    for i in l:
        if(i%2==0):
            evenList.append(i)
        else:
            oddList.append(i)
    return evenList,oddList


l=[10,20,31,40,50,60]

even,odd=evenOdd(l)

print("Even List is: ",even)
print("Even Odd List is: ",odd)