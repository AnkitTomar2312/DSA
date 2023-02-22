#Palindrome Number
n=int(input("Enetr n: "))
var=n
res=0
while(var!=0):
    ld=var%10
    res=res*10+ld
    var=var//10

if(n==res):
    print("yes")
else:
    print("no")