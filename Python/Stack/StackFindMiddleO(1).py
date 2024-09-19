# A Doubly Linked List Node
class DLLNode:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

# Representation of the stack data structure that supports findMiddle() in O(1) time.
class MyStack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.size = 0

    # Function to push an element to the stack
    def push(self, new_data):
        new_node = DLLNode(new_data)

        if self.size == 0:  # if stack is empty
            self.head = new_node
            self.mid = new_node
        else:
            self.head.next = new_node
            new_node.prev = self.head
            self.head = new_node

            # Update mid pointer if size is odd
            if self.size % 2 != 0:
                self.mid = self.mid.next

        self.size += 1

    # Function to pop an element from the stack
    def pop(self):
        if self.size == 0:
            print("Stack is empty")
            return -1

        data = self.head.data
        if self.size == 1:
            self.head = None
            self.mid = None
        else:
            self.head = self.head.prev
            self.head.next = None

            # Update mid pointer if size is even
            if self.size % 2 == 0:
                self.mid = self.mid.prev

        self.size -= 1
        return data

    # Function to find the middle element of the stack
    def find_middle(self):
        if self.size == 0:
            print("Stack is empty now")
            return -1
        return self.mid.data

    # Function to delete the middle element
    def delete_middle_element(self):
        if self.size == 0:
            return

        if self.size == 1:
            self.head = None
            self.mid = None
        elif self.size == 2:
            self.head = self.head.prev
            self.mid = self.mid.prev
            self.head.next = None
        else:
            # Link the previous and next nodes of the middle node
            self.mid.prev.next = self.mid.next
            if self.mid.next:
                self.mid.next.prev = self.mid.prev

            # Update the mid pointer
            if self.size % 2 == 0:
                self.mid = self.mid.prev
            else:
                self.mid = self.mid.next

        self.size -= 1

# Driver code to test the MyStack class
if __name__ == '__main__':
    ms = MyStack()
    ms.push(11)
    ms.push(22)
    ms.push(33)
    ms.push(44)
    ms.push(55)
    ms.push(66)
    ms.push(77)
    ms.push(88)
    ms.push(99)

    print("Popped:", ms.pop())
    print("Popped:", ms.pop())
    print("Middle Element:", ms.find_middle())
    ms.delete_middle_element()
    print("New Middle Element:", ms.find_middle())
