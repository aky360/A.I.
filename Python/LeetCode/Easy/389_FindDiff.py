
from collections import * 

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)                               # Counter('string')  returns the dictionary with key string char to value is its counts (no. of string char)

        for i, c in enumerate(t):
            count[c] -= 1
            if count[c] == -1:
                return c


            
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference('abcd', 'abcde'))
