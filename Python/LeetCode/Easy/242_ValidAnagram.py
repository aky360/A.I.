
from collections import * 
            
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(s), Counter(t)
        
        if((len(s) == len(t)) and (sCount == tCount)):
            return True
        return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        #return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i], 0)
            countT[t[i]] = 1+countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
        
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram('abcd', 'abcde'))
    print(sol.isAnagram('anagram', 'nagaram'))
    print(sol.isAnagram('rat', 'car'))
