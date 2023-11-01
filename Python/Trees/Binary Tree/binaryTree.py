'"Binary Tree Class and its methods"' 
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    #set data 
    def setData(self, data): 
        self.data = data 
    #get data 
    def getData(self): 
        return self.data 
    #get left child of a node 
    def getLeft(self): 
        return self.left
    #get right child of a node 
    def getRight(self): 
        return self.right
