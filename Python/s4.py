#Factorial of the number
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))


# Iterative Approach
# def fact(n):
#     res=1
#     for i in range(2, n+1):
#         res=res*i
#     return res
# if __name__ == '__main__':
#     number=5
#     print(fact(number))