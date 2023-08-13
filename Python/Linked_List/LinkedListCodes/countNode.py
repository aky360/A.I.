
def listLength(self): 
    current = self.head 
    count = 0 
    while current != None: 
        count += 1
        current = current.getNext() 
    return count 
