
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
previousnode. seNcxt(Nonc) 
self. length -= 1



##Delete with node from linked list 
def dcletcFromLinkcdListWithNodc(self, node): 
if self. length ..... 0: 
raise ValueE1Tor("List is empty") 
else: 
current= self.head 
previous = None 
found = False 
while not found: 
if current node: 
found .. True 
c lif current is None: 
t 
Node to be deleted 
else: 
ra ise ValucError("Nodc not in Linked List") 
previous = current 
current"' currenl.gelNext() 
if previous is None: 
else: 
self.head • current.gclNcxl() 
previous.scNcxt(current.getNextQ) 
self.length -= 1 
#Delete with data from linked list 
def dclctcValuc(sclf, value): 
currcntnodc self.head 
prcviousnodc self.head 
while currentnode.next != None or currentnode.value !•value: 
if currcntnodc. value == value: 
prev1ousnode.next = currentnode.next 
self.length -• l 
return 
else: 
prev10usnode "' currentnodc 
currcnlnodc currentnodc.nexl 
print "The vnluc provided is not present~ 
#Mel hod lo delete a node al a particular position 
def dcleleALPosition(sclf,pos): 
count = 0 
3.6 Singly Linked List
