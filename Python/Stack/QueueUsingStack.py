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
