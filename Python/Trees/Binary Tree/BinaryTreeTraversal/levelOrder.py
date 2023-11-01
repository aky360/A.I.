import Queue 
def levelOrder(root, result):
    if(root is None): 
        return 
    q = Queue.Queue() 
    q.put(root) 
    node = None 
    while(not q.empty()): 
        node = q.get()
        result.append(node.getData()) 
        if(node.getLeft() is not None): 
            q.put(node.getLeft()) 
        if(node.getRight() is not None): 
            q.put(node.getRight()) 
