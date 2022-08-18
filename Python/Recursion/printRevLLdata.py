class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class Solution:
    def reverseList(self, head):
        li = head
        
        if(head == None):
            return 
        
        if(li == None):
            return 
        
        self.reverseList(li.next)
        print(li.data)
    
    def printList(self, head):
        temp = head
        while(temp != None):
            print(temp.data)
            temp = temp.next
        
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)

sol = Solution()
sol.reverseList(root)
