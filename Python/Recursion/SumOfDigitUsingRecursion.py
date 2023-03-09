def Sum(n):
    if n<10:
        return n
    return Sum(n//10)+n%10


print(Sum(253))