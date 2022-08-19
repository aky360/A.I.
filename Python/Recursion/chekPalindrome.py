#This checks the number is palindrome or not 
def numPalindrome(num):
    reverse = 0
    temp = num
    
    while temp != 0:
        reverse = reverse*10 + temp%10
        temp = temp//10
    
    if num == reverse:
        return "palindrome"
    
    return "not palindrome"
        
     
num = 12321
nums = 123454321
print(numPalindrome(num))
print(numPalindrome(nums))


#check string palindrome using start and end index
def strPalindrome(strs, s, e):
    if(s > e):
        return True
    if len(strs)==0:
        return False
    if(strs[s] == strs[e]):
        print(strs[s],' ', strs[e])
        return strPalindrome(strs, s+1, e-1)
    return False
    
    
st = 'abcba'
print(strPalindrome(st, 0, 4))
     
    
#check string palindrome using start index
def strPalindrome(strs, i):
    if(i > len(strs)-1-i):
        return True
    if len(strs)==0:
        return False
    if(strs[i] == strs[len(strs)-1-i]):
        return strPalindrome(strs, i+1)
    return False

st = 'dabcbad'
print(strPalindrome(st, 0))
