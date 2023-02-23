# To Find Prime Fctorization

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def printPrimeFactors(n):
    for i in range(2,n+1):
        if  isPrime(i):
            x=i
            while  n%x==0:
                print(i)
                x=x*i

printPrimeFactors(100)