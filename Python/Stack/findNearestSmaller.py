class Solution:
    
    def __init__(self):
        self.stack = []
    
    def findNearestSmallest(self, arr, n):
        s = []
        for i in range(n):
            
            while self.stack and self.stack[-1]>arr[i]:
                self.stack.pop()
            
            if self.stack:
                s.append(self.stack[-1])
            else:
                s.append('-')
            
            self.stack.append(arr[i])
        
        return s
   
#   def __str__(self):
#       self.stack = s
#       return str(self.stack)
        
# Driver code
if __name__ == '__main__':
    arr = [1, 6, 4, 10, 2, 5]
    sol = Solution()
    print(sol.findNearestSmallest(arr,6))
   
