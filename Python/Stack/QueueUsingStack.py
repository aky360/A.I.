# Python3 program to implement Queue using 
# two stacks with costly enQueue() 

class Queue: 
	def __init__(self):
		self.s1,self.s2  = [],[]

	def enQueue(self, x):
		while self.s1: self.s2.append(self.s1.pop())
		self.s1.append(x)
		while self.s2: self.s1.append(self.s2.pop()) 
			
	def deQueue(self):
		if len(self.s1) == 0: return -1;
		return self.s1.pop() 
		
	def __str__(self): return str(self.s1)

# Driver code 
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1) 
	q.enQueue(2) 
	q.enQueue(3) 
	
	print(q)

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())

============================================================================================================================

# Python3 program to implement Queue using 
# two stacks with costly deQueue()

class Queue:
	def __init__(self):
		self.s1,self.s2 = [],[]

	def enQueue(self, x):
		self.s1.append(x)

	def deQueue(self):
		if len(self.s1) == 0 and len(self.s2) == 0:
			return -1

		elif len(self.s2) == 0 and len(self.s1) > 0:
			while len(self.s1):
				self.s2.append(self.s1.pop())
			return self.s2.pop()

		else:
			return self.s2.pop()
			
	def __str__(self):
	    return str(self.s1)

	# Driver code
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)
	
	print(q)

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())

============================================================================================================================

# Python3 program to implement Queue using 
# one stack and recursive call stack. 
class Queue:
	def __init__(self): self.s = []
		
	def enQueue(self, data):
		self.s.append(data)
		
	def deQueue(self):
		# Return if queue is empty
		if len(self.s) <= 0:
			return -1
		
		# pop an item from the stack
		x = self.s[len(self.s) - 1]
		self.s.pop()
		
		# if stack become empty
		# return the popped item
		if len(self.s) <= 0:
			return x
			
		# recursive call
		item = self.deQueue()
		
		# push popped item back to
		# the stack
		self.s.append(x)
	
		# return the result of 
		# deQueue() call
		return item
	
	def __str__(self): return str(self.s)
	
# Driver code 
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)
	
	print(q)
	
	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue()) 

===========================================================================================================================

# Python3 program to implement Queue using 
# one stack and recursive call stack. 
class Queue:
	def __init__(self): self.s = []
		
	def enQueue(self, data):
		self.s.append(data)
		
	def deQueue(self):
		# Return if queue is empty
		if len(self.s) == 0: return -1
		return self.s.pop(0)
	
	def __str__(self): return str(self.s)
	
# Driver code 
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)
	
	print(q)
	
	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())
	
	print(q)
