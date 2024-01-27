x=int(input("Enter a number: "))
counter=0
while x>0:
    x=x//10
    counter+=1
print(counter)