
# Program to implement a stack using
# two queue
from _collections import deque

class Stack:

    def __init__(self):
        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):

        # Push x first in empty q2
        self.q2.append(x)

        # Push all the remaining
        # elements in q1 to q2.
        while (self.q1):
            self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):

        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()

    def top(self):
        if (self.q1):
            return self.q1[0]
        return None

    def size(self):
        return len(self.q1)


# Driver Code
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("current size: ", s.size())

============================================================================================================================

# Program to implement a stack using
# two queue
from _collections import deque

class Stack:

    def __init__(self):
        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        # if no elements are there in q1
        if (not self.q1):
            return
        # Leave one element in q1 and push others in q2
        while(len(self.q1) != 1):
            self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def top(self):
        # if no elements are there in q1
        if (not self.q1):
            return
        # Leave one element in q1 and push others in q2
        while(len(self.q1) != 1):
            self.q2.append(self.q1.popleft())

        # Pop the only left element from q1 to q2
        top = self.q1[0]
        self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

        return top

    def size(self):
        return len(self.q1)


# Driver Code
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("current size: ", s.size())

===========================================================================================================================

from _collections import deque
# Stack Class that acts as a queue

class Stack:
    def __init__(self):
        self.q = deque()

    # Push operation
    def push(self, data):
        # Get previous size of queue
        s = len(self.q)

        # Push the current element
        self.q.append(data)

        # Pop all the previous elements and put them after
        # current element
        for i in range(s):
            self.q.append(self.q.popleft())

    # Removes the top element
    def pop(self):
        if (not self.q):
            print("No elements")
        else:
            self.q.popleft()

    # Returns top of stack
    def top(self):
        if (not self.q):
            return
        return self.q[0]

    def size(self):
        return len(self.q)


if __name__ == '__main__':
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print("current size: ", st.size())
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
    print("current size: ", st.size())
