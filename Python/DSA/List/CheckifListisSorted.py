def isSorted(arr,n):
    ascendingSorted=True
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            ascendingSorted=False
            break
    descendingSorted=True
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            descendingSorted=False
            break
    if ascendingSorted or descendingSorted:
        return 1
    else:
        return 0
        
arr=[
490,656,941,731,992,480,20,770,19,319,795,79,38,559,923,6,515,196,915,153,288,529,358,674,107,85,731,584,304,174,341,853,952,188,317,327,780,281,660,477,738,512,365,341,791,204,210,411,142,194,798,68,224,41,571,940,452,168,93,773,289,858,463,578,218,310,84,587,217,753,49,49,831,592,17,124,50,880,584,290,209,193,308,723,676,331,609,19,119,543,725,632,504,185,92,461,127,157,100,134,622,287,506,717,257,639,239,85,504,717,478,540,914,106,759,534,821,295,977,663,811,449,723,993,38,478,692,304,848,257,203,946,260,52,185,219,1,126,503,535,712,691,386,793,324,76,214,804,706,142,473,824,25,895,935,576,691,366,327,105,268,835,147,349,803,295,69,25,535,988,729,604,411,856,174,953,685,175,185,422,92,855,35,262,48,208,121,988,598,27,661,602,68,273,971,328,26,40,743,344,426,554,821,842,441,278,536,124,110,867,399,932,842,34,358,169,657,484,25,422,840,948,886,33,951,654,323,219,882,623,85,656,962,615,363,618,353,333,2,913,662,849,266,694,461,520,809,8,651,979,607,191,137,161,866,678,646,751,907,942,962,461,112,409,224,891,923,956,36,243,163,201,198,440,713,724,397,768,518,980,391,342,43,260,615,11,457,715,905,502,571,73,267,745,672,787,548,262,517,232,553,474,211,836,133,425,580,389,969,242,516,789,724,684,190,416,509,153,188,895,735,2,915,307,204,748,142,245,829,537,145,406,377,105,937,634,836,283,923,947,369,719,363,339,60,46,654,98,761,556,345,937,705,812,219,157,54,748,800,208,452,987,720,629,387,225,967,219,538,118,782,4,967,53,987,342,524,626,724,865,652,962,122,530,638,650,515,327,504,643,224,604,825,508,672,334,800,1,756,646,656,34,646,753,304,879,148,941,806,90,905,326,405,429,5,634,847,935,515,337,652,337,588,97,146,997,347,913,543,913,824,477,702,992,449,809,263,906,438,554,386,726,915,817,116,93,316,177,971,8,380,595,231,812,670,319,410,205,71,38,185,449,60,542,907,183,880,142,434,856,281,331,463,820,460,186,291,864,973,590,907,607,252,92,851,366,540,709,327,116,158,805,166,714,182,874,296,959,772,302,745,832,933,160,798,286,155,472,608,968,498,810,807,467,260,245,600,302,640,373,170,875,63,893,333,819]
n=len(arr)
print(isSorted(arr,n))




 # aS=sorted(arr)
    # dS=list(reversed(arr))
    # print(aS)
    # if aS==arr:
    #     return "ascending order"
    # elif dS==arr:
    #     return "descending order"
    # else: return False
    # i=1
    # while i<len(arr):
    #     if arr[i]<arr[i-1]:
    #         return False
    #     else:
    #         return True