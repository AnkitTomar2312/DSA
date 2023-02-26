#All Divisors of a Number

#Naive Approach
# TC=>theta(n)
# Ac=>theta(1)

# def printDivisor(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
 
# printDivisor(5)




#Efficient Approach
#Print all the divisors but not in necessary order

# def printDivisor(n):
#     i=1
#     while(i*i<=n):
#         if(n%i==0):
#             print(i)
#             if(i!=n//i):
#                 print(n//i)
#         i+=1

# printDivisor(125)

#Efficient Approach
#Print all the divisors in necessary order:


def printDivisors(n):
    i=1
    while(i*i<n):
        if(n%i==0):
            print(i)
        i+=1
    while(i>=1):
        if(n%i==0):
            print(n//i)
        i-=1

printDivisors(12)