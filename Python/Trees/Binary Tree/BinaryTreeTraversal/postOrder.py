# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postOrderRecursive(root, result):
    if(not root): 
        return
    postOrderRecursive(root.left, result) 
    postOrderRecursive(root.right, result) 
    result.append(root.data) 


""" Post-order iterative traversal. The nodes' values are appended to the result list in traversal order """
def postOrder_Iterative(root, result):
    if(not root): 
        return
    visited = set() 
    stack = [] 
    node = root 
    while(stack or node): 
        if(node): 
            stack.append(node) 
            node = node.left 
        else: 
            node = stack.pop() 
            if(node.right and not node.right in visited): 
                stack.append(node) 
                node = node.right 
            else: 
                visited.add(node) 
                result.append(node.data) 
                node = None 
