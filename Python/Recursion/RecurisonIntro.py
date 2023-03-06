#-->A funciton calls itself directly or Indirectly<--

# def fun1():
#     print('fun1() called')
# def fun2():
#     print('Before fun1() called')
#     fun1() #indirect call 
#     print('After fun1() called')
# print('Before fun2() called')
# fun2()
# print('After fun2() called')



#Direct recurive program:
def fun3(n):
    if n==0:
        return
    print("GFG")
    fun3(n-1)
fun3(5)