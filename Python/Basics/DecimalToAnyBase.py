

class Solution:
    def getNumber(self, Base, Number):
        ans = ''
        while Number:
            remainder = Number%Base
            if remainder >= 10:
                ans = chr(55+remainder)+ans
            else:
                ans = str(remainder)+ans
            Number //= Base
        return ans


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.getNumber(2, 12))
      
