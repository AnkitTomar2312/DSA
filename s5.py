# Trailing Zeros in Factorial

#Naive solution

# def countZeros(n):
#     fact=1
#     for i in range(2,n+1):
#         fact=fact*i
#     res=0
#     while(fact%10==0):
#         res+=1
#         fact=fact//10
#     return res

#Smart Solution
def countZeros(n):
    res=0
    while(n>=5):
        n//=5
        res+=n
    return res
print(countZeros(251))