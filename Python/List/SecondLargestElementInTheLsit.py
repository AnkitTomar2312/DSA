def getMax(list1):
    res=list1[0]
    for i in range(1,len(list1)):
        res=max(res,list1[i])
    return res


def findSecondLargest(list1):
    if(len(list1)<=1):
        return None
    else:
        f_lar = getMax(list1)
       
        s_lar = None
        for i in list1:
            if f_lar is not i:
                if s_lar is None:
                    s_lar=i
                    
                else:
                    s_lar=max(s_lar,i)
                    
        return s_lar




print("This is a Solution of  Double travesal")
list1 = [10,20,30,60,80,40,50]
print(findSecondLargest(list1))



#single treversl Approach
def singleTraversalGetMax(list2):
    if len(list2)<=1:
        return None
    f_lar=list2[0]
    s_lar=None
    for i in list2[1:]:
        if i>f_lar:
            s_lar=f_lar
            f_lar=i
        elif i is not f_lar:
            if s_lar==None or s_lar<i:
                s_lar=i
    return s_lar
print("This is a solution of Single Traversal")
list2 = [10,20,30,60,80,40,50]
print(singleTraversalGetMax(list2))