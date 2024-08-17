# Python program to evaluate the value of a postfix expression
# Class to evaluate postfix expressions
class Evaluate:

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = []

    def isEmpty(self):
        return len(self.array) == 0

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.array.append(op)

    def evaluatePostfix(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(int(i))
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(eval(f'{val2} {i} {val1}'))

        return self.pop()
        
# Driver code
if __name__ == '__main__':
    postfix_exp = '100 200 + 2 / 5 * 7 +'
    expr = "231*+9-"
    exp =''
    if ' ' in postfix_exp:
        exp = postfix_exp.split()
    obj = Evaluate(len(exp))
    obj2 = Evaluate(len(expr))

    print("Postfix evaluation: %d" % (obj.evaluatePostfix(exp)))
    print("Postfix evaluation: %d" % (obj2.evaluatePostfix(expr)))

===============================================================================================================================

class evalpostfix:
	def __init__(self):
		self.stack = []
		self.top = -1

	def pop(self):
		if self.top == -1:
			return
		else:
			self.top -= 1
			return self.stack.pop()

	def push(self, i):
		self.top += 1
		self.stack.append(i)

	def evaluatePostfix(self, ab):
		for i in ab:
			try:
				self.push(int(i))
			except ValueError:
				val1 = self.pop()
				val2 = self.pop()
				self.push(eval(f'{val2} {i} {val1}'))
		return int(self.pop())

# Driver code
if __name__ == '__main__':
	str = '100 200 + 2 / 5 * 7 +'
	strconv = str.split(' ')
	obj = evalpostfix()
	print(obj.evaluatePostfix(strconv))
