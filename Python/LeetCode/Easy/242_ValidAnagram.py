
from collections import * 
            
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(s), Counter(t)
        
        if((len(s) == len(t)) and (sCount == tCount)):
            return True
        return False
        
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram('abcd', 'abcde'))
    print(sol.isAnagram('anagram', 'nagaram'))
    print(sol.isAnagram('rat', 'car'))
