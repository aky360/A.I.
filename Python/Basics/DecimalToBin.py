

class Solution:
    def getBinNumber(self, Base, Number):
        ans = ''
        while Number:
            remainder = Number%Base
            ans = str(remainder)+ans
            Number //= Base
        return ans


class Solution:
    def getBinNumber(self, Base, Number):
        ans = ''
        while Number:
            remainder = Number%Base
            ans = ans+str(remainder)
            Number //= Base
        return ans[::-1]


class Solution:
    def getBinNumber(self, Base, Number):
        ans = ''
        while Number:
            ans = str(Number&1) + ans
            Number //= Base
        return ans


class Solution:
    def dec2Bin(self, B, N):
        ans=""
        while N:
            ans += str(N&1)
            N = N >> 1
        ans = ans[::-1]
        return ans
        
    def dec2Bin(self, B, N):
        ans=""
        while N:
            ans = str(N&1)+ans
            N = N >> 1
        return ans


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.getNumber(2, 100))
    print(bin(100)[2:])
