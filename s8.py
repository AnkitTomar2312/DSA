#Check for Prime Number

#Naive Approach
# def isPrime(n):
#     if n==1:
#         return False
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True
    
# print(isPrime(5))


#TC=> O(n)

#Optimized Approach

# def isPrime(n):
#     if n==1:
#         return False
#     i=2
#     while(i*i<=n):
#         if n%i==0:
#             return False
#         i+=1
#     return True

# print(isPrime(37))

#Super Efficient Approach

def isPrime(n):
    if  n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<=n):
        if(n%i==0 or n%(i+1)==0):
            return False
        i+=6
    return True

print(isPrime(5))