# Python3 program to implement Queue using 
# one stack and recursive call stack. 

from _collections import deque
class Stack:
    
    def __init__(self):
        self.q=deque()
    
    def push(self,x):
        size = len(self.q)
        # Add current element 
        self.q.append(x)
        # Pop (or Dequeue) all previous elements and put them after current element
        for i in range(size):
            # this will add front element into rear of queue 
            self.q.append(self.q.popleft())
    
    def pop(self):
        if len(self.q)==0:
            return -1
        return self.q.popleft()
    
    def __str__(self): return str(self.q)
--------------------------------------------------------------------------------------------------------------------------------------------------------------
class Stack:
    
    def __init__(self):
        self.q=[]
    
    def push(self,x):
        size = len(self.q)
        # Add current element 
        self.q.append(x)
        # Pop (or Dequeue) all previous elements and put them after current element
        for i in range(size):
            # this will add front element into rear of queue 
            self.q.append(self.q.pop(0))
    
    def pop(self):
        if len(self.q)==0:
            return -1
        return self.q.pop(0)
    
    def __str__(self): return str(self.q)
	
# Driver code 
if __name__ == '__main__':
	q = Stack()
	q.push(1)
	q.push(2)
	q.push(3)
	
	print(q)
	
	print(q.pop())
	print(q.pop())
	print(q.pop())
