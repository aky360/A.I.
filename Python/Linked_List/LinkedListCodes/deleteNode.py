
#method to delete the first node of the linked list 
def deleteFromBeginning(self):
    if self.length == 0:
        print("The list is empty")
    else: 
        self.head = self.head.getNext()
        self.length -= 1 


# Method to delete the last node of the linked list 
def deleteLastNodeFromSinlyLinkedList(self):
    if self.length == 0:
        print("The list is empty")
    else: 
        currentnode = self.head 
        previousnode = self.head 
    while currentnode.getNext() != None: 
        previousnode = currentnode 
        currentnode = currentnode.gctNext() 
    previousnode.seNext(None) 
    self.length -= 1



##Delete with node from linked list 
def deleteFromLinkedListWithNode(self, node):
    if self.length == 0:
        raise ValueError("List is empty") 
    else:
        current= self.head 
        previous = None 
        found = False 
        while not found:
            if current == node:
                found = True 
            elif current is None:
                raise ValueError("Node not in Linked List") 
            else:
                previous = current 
                current = current.gelNext() 
    if previous is None:
        self.head = current.getNext() 
    else:
        previous.setNext(current.getNext()) 
    self.length -= 1 
    
#Delete with data from linked list 
def deleteValue(self, value): 
    currentnode = self.head 
    previousnode = self.head 
    while currentnode.next != None or currentnode.value != value:
        if currentnode.value == value:
            previousnode.next = currentnode.next 
            self.length -= 1 
            return 
        else:
            previousnode = currentnode 
            currentnode = currentnode.next 
    print("The vnlue provided is not present")
    
#Method lo delete a node at a particular position 
def deleleAtPosition(self,pos):
    count = 0
    currentnode = self.head 
    previousnode = self.head 
    if pos > self.length or pos < 0: 
        print("The position does not exist. Please enter a valid position") 
    else:
        while currentnode.next != None or count < pos:
            count = count + 1 
            if count == pos: 
                previousnode.next = currentnode.next 
                self.length -= 1 
                return 
            else: 
                previousnode = currentnode 
                currentnode = currentnode.next 
