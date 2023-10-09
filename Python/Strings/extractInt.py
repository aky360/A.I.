
class Solution:
    def extractIntegerWords(self, s):
        temp,ans ="",[]
        for i in range(len(s)):
            if len(temp) > 0:
                if s[i].isnumeric() == False:
                    ans.append(temp)
                    temp=""
            if s[i].isnumeric(): temp+=s[i]
                if len(s)-1 == i: ans.append(temp)
        return ans
