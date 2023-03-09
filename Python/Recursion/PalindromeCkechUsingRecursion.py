def isPalindrome(str,start,end):
    if start>end:
        return True
    return (str[start]==str[end] and isPalindrome(str,start+1,end-1))

print(isPalindrome("abcba",0,4))