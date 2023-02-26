#GDC of two number
#Euclead Algorithm


#NaiveApproach
# def gdc(a,b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#         return a
    
# print(gdc(5,10))



#Optimised Approach

def gdc(a,b):
    if(b==0):
        return a
    return gdc(b,a%b)
print(gdc(12,15))