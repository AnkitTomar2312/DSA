# Program 1

print("Printing Program 1: \n")
def pro1(n):
    if n==0:
        return 
    print(n)
    pro1(n-1)
    print(n)

pro1(3)

# Program 2:
print("Printing Program 2: \n")
def pro2(n):
    if n==0:
        return
    pro2(n-1)
    print(n)
    pro2(n-1)


pro2(3)