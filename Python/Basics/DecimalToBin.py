

class Solution:
    def getNumber(self, Base, Number):
        ans = ''
        while Number:
            remainder = Number%Base
            ans = str(remainder)+ans
            Number //= Base
        return ans
    
    
if __name__ == "__main__":
    Sol = Solution()
    print(Sol.getNumber(2, 100))
    print(bin(100)[2:])
