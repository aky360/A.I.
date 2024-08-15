# Python program to evaluate the value of a postfix expression

# Class to evaluate postfix expressions
class Evaluate:

    def __init__(self, capacity):
        self.capacity = capacity
        # This array is used as a stack
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

    # The main function that evaluates a given postfix expression
    def evaluatePostfix(self, exp):
        # Iterate over the expression for every character
        for i in exp:
            # If the character is a digit, push it to the stack
            if i.isdigit():
                self.push(int(i))
            else:
                # Pop two elements from the stack for the operator
                val1 = self.pop()
                val2 = self.pop()
                switcher = {
                            '+': val2 + val1, 
                            '-': val2 - val1, 
                            '*': val2 * val1, 
                            '^': val2**val1,
                            '/': val2 / val1
                }
                self.push(switcher.get(i))
                # OR 
                # self.push(switcher[i])

        return self.pop()
        
# Driver code
if __name__ == '__main__':
    # Postfix expression with spaces separating elements
    postfix_exp = '100 200 + 2 / 5 * 7 +'
    expr = "231*+9-"
    exp =''
    if ' ' in postfix_exp:
        # Split the expression into a list
        exp = postfix_exp.split()
    # Create an object of the Evaluate class with a size equal to the expression length
    obj = Evaluate(len(exp))
    obj2 = Evaluate(len(expr))

    # Evaluate the postfix expression
    print("Postfix evaluation: %d" % (obj.evaluatePostfix(exp)))
    print("Postfix evaluation: %d" % (obj2.evaluatePostfix(expr)))
