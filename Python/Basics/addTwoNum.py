"""
Add two numbers without using arithmetic operators (+, -)
"""

class Add:
    
    def addTwo(self, x, y):
        for i in range(1, y+1):
            x += 1
            
        return x
        
        
    def addTwoItr(self, x, y):
        # Iterate till there is no carry
        while (y != 0):
        # carry now contains common
        # set bits of x and y
            carry = x & y
        # Sum of bits of x and y where at
        # least one of the bits is not set
            x = x ^ y
        # Carry is shifted by one so that  
        # adding it to x gives the required sum
            y = carry << 1
            # print(carry, ' ', x, ' ', y)
        return x
    
    
    def addTwoRec(self, x, y):
        if(y==0):
            return x
            
        return self.addTwoRec(x^y, (x&y)<<1)
    
    
    # leetcode solution for sum of two integer 
    def getSum(a: int, b: int) -> int:
        while(a!=0 and b!=0):
            an = a&b
            xor = a^b
            a = an<<1
            b = xor
        if(a!=0):
            return a
        else:
            return b
    
        
        
add = Add()
    
print(add.addTwo(1, 23))
print(add.addTwoItr(1, 23))
print(add.addTwoRec(1, 23))
