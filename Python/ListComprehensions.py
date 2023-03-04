#Given a list and a number x find the list of numbers smaller than x

def findSmaller(l,n):
    return [e for e in l if e<n]


l=[10,20,30,40,50,60,70,81]
n=40
print(findSmaller(l,n))

#Return the list of a odd number and even number

def evenOdd(l):
    even=[i for i in l if i%2==0]
    odd=[i for i in l if i%2!=0]
    return even,odd

print(evenOdd(l))