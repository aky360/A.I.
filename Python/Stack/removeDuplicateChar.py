
class Solution:
    NO_OF_CHARS = 256
     
    def getCharCountArray(self, string):
        count = [0] * Solution.NO_OF_CHARS
        for i in string:
            count[ord(i)] += 1
        return count
        
        
    def removeChars(self,string, mask_string):
        count = self.getCharCountArray(mask_string)
        actualStr_index = 0
        resultStr_inded = 0
        temp = ''
        str_list = list(string)
       
        while actualStr_index != len(str_list):
            temp = str_list[actualStr_index]
            if count[ord(temp)] == 0:
                str_list[resultStr_inded] = str_list[actualStr_index]
                resultStr_inded += 1
            actualStr_index += 1
        return ''.join(str_list[0:resultStr_inded])
        
    # OR
        
    def removeChars(self, string, mask_string):
        res = ''
        for i in string:
            if i not in mask_string:
                res+=i
        return res
        
    # OR
        
    def removeChars(self,string1, string2): return ''.join([char for char in string1 if char not in set(string1)&set(string2)])
    
    # OR
    
    def removeChars(self,s1,s2):
        res = ""
        n1,n2=len(s1),len(s2)
        arr = [0] * 26
     
        for i in range(0, n2):
            arr[ord(s2[i]) - ord('a')] = -1 
            
        for i in range(0, n1):
            if (arr[ord(s1[i]) - ord('a')] != -1):
                res += s1[i]
                
        return res
    
if __name__ == "__main__":

	post_exp = "ABC/-AK/L-*"
	print(''.join(list(post_exp)))
	
	string1 = 'occurrence'
	string2 = 'car'
	
	s1=set(string1)
	print(s1)
	s2=set(string2)
	print(s2)
	s=s1&s2
	print(s)
	
	sol=Solution()
	print(sol.removeChars(string1,string2))
	
