#factorial of n  where n>=0

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

print(fact(5))



#Fibonacci Number

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(3))