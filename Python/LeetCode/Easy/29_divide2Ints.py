'''
29. Divide Two Integers
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # MAX and MIN values for integer
        MAX = 2147483647
        MIN = -2147483648
        # Check for overflow
        if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX
        # Sign of result`
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        # Quotient
        quotient = 0
        # Take the absolute value
        absoluteDividend = abs(dividend)
        absoluteDivisor = abs(divisor)
        # Loop until the  dividend is greater than divisor
        while absoluteDividend >= absoluteDivisor:
            # This represents the number of bits shifted or
            # how many times we can double the number
            shift = 0
            while absoluteDividend >= (absoluteDivisor << shift):
                print(" condition shift ",(absoluteDivisor << shift))
                shift += 1
                print('shift ', shift)
            # Add the number of times we shifted to the quotient
            quotient += (1 << (shift - 1))
            print('quotient ', (1 << (shift - 1)), ' ', quotient)
            # Update the dividend for the next iteration
            absoluteDividend -= absoluteDivisor << (shift - 1)
            print('absoluteDividend ', absoluteDividend, ' ', absoluteDivisor << (shift - 1))
        return -quotient if sign == -1 else quotient
    
        
sol = Solution()
if __name__ == '__main__':
    print(sol.divide(10, -3))
