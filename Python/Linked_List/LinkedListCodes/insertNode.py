
#method for inserting a new node at the beginning of the Linked List (at the head) 
def insertAtBeginning(self,data): 
    newNode = Node() 
    newNode.setData(data) 
    if self.length == 0:
        self.head = newNode 
    else: 
        newNode.setNext(self.head) 
        self.head = newNode 
    self.length += 1



#method for inserting a new node at the end of a Linked List 
def insertAtEnd(self,data): 
    newNode = Node()     
    newNode.setData(data)
    current= self.head 
    while current.getNext() != None: 
        current = current.getNext() 
    current.setNext(newNode) 
    self.length += 1



#Method for inserting a new node a t a ny position in a Linked List 
def insertAtPos(self, pos, data):
    if pos > self.length or pos < 0: 
        return None 
    else:
        if pos == 0:
            self.insertAtBeginning(data) 
        else:
            if pos == self.length:
                self.insertAtEnd(data) 
            else: 
                newNode = Node() 
                newNode.setData(data) 
                count = 0 
                current = self.head 
                while count < pos-1: 
                    count += 1 
                    current = current.getNext() 
                newNode.setNext(current.getNext()) 
                current.setNext(newNode) 
                self.length += 1
