class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    
def buildTree(root):
    data = int(input())
    root = Node(data);   
    
    if data ==-1:
        return None
        
    print("Enter data for inserting in left of ", data)
    root.left = buildTree(root.left)
    print("Enter data for inserting in right of ", data)
    root.right = buildTree(root.right)
    
    return root
        
        
root = None
buildTree(root)
