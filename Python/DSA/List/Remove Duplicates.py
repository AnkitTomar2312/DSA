list=[10,20,20,20,30,30,30,40,40,40]
n=len(list)




def RemoveDupli(list,n):
    res=1
    for i in range(1,n):
        if list[res-1]!=list[i]:
            list[res]=list[i]
            res+=1
    return res

    # arr=[0]*n
    # res=1
    # arr[0]=list[0]
    # for i in range(1,n):
    #     if arr[res-1]!=list[i]:
    #         arr[res]=list[i]
    #         res+=1
    # for i in range(0,res):
    #     list[i]=arr[i]
    # return res


print(RemoveDupli(list,n))