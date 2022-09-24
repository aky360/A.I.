'''
844. Backspace String Compare
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.stringCompare(s) == self.stringCompare(t)
        
    def stringCompare(self, s: str):
        chars = []
        for char in s:
            print(char)
            if char == "#" and len(chars) >= 1:
                print(chars.pop())
            else:
                if "#" in chars:
                    print(chars.pop())
                chars.append(char) 
                print(chars)
        return chars
        
        
        
if __name__=="__main__":
    x = Solution()
    print(x.backspaceCompare("ab#c", "ad#c"))
