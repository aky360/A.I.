
class Solution:
    NO_OF_CHARS = 256
     
    def getCharCountArray(self, string):
        count = [0] * Solution.NO_OF_CHARS
        for i in string:
            count[ord(i)] += 1
        return count
        
        
    def removeDirtyChars(self,string, mask_string):
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


if __name__ == "__main__":

	post_exp = "ABC/-AK/L-*"
	print(''.join(list(post_exp)))
	string1 = 'computer'
	string2 = 'cat'
	sol=Solution()
	print(sol.removeDirtyChars(string1,string2))

