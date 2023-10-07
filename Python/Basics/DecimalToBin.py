

class Solution:
    def getBinNumber(self, Base, Number):
        ans = ''
        while Number:
            remainder = Number%Base
            ans = str(remainder)+ans
            Number //= Base
        return ans


class Solution2:
    def getBinNumber(self, Base, Number):
        ans = ''
        while Number:
            remainder = Number%Base
            ans = ans + str(remainder)
            Number //= Base
        return ans[::-1]
    
    
if __name__ == "__main__":
    Sol = Solution()
    print(Sol.getNumber(2, 100))
    print(bin(100)[2:])
