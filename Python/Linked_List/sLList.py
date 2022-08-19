class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
    def builtLinkedList(self, head):
        data = int(input('enter data '))
        head = LinkedList(data)
        temp = head
        while temp != None:
            data = int(input('enter data '))
            temp.next = LinkedList(data)
            if temp.data == -1:
                temp.next = None
                return head
            temp = temp.next
        return head
        
    def printLList(self, head):
        if not head or not head.next:
            return head
            
        temp = head
        while temp != None:
            print("temp data ", temp.data)
            temp = temp.next
        

# root = LinkedList(1)
# root1 = LinkedList(2)
# root2 = LinkedList(3)
# root3 = LinkedList(4)

# root.next = root1
# root1.next = root2
# root2.next = root3
# root3.next = None

head  = None
root = LinkedList(head)
head = root.builtLinkedList(root)
root.printLList(head)
