#A function is called as a tail recursive if the function does not do any thing after the last recursive call

#Python does not do the tail call elimination

# example: quick Sort, post Order tree traversals
def fun(n):
    if n==0:
        return 0
    print(n)
    fun(n-1)

fun(5)

# In python we can do the change just by removing the rescursion and adding while loop 
# and changing the calues of parameters at the end

def fun1(n):
    while(n>0):
        print(n)
        n-=1
fun1(5)