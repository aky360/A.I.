
#Node of a Singly Linked List 
class Node: 
    #constructor 
    def __init__(self): 
        self.data = None 
        self.next s None 
        
    #method for setting the data field of the node 
    def setData(self,data): 
        self.data = data 
        
    #method for getting the data field of the node
    def getData(self): 
        return self.data 
        
    #method for setting the next field of the node 
    def setNext(self,next): 
        self.next = next 
        
    #method for getting the next field of the node 
    def getNext(self): 
        return self.next 
        
    #returns trne if the node points to another node 
    def hasNext(self): 
        return self.next != None 
