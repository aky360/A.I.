# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        if(head == None):
            return head
        
        curr = head
        curr.next = None
        head = head.next
        prev = head
        
        while(head != None):
            if(head.next == None):
                head.next = curr
                return curr
            head = prev.next
            prev.next = None
            prev.next = curr
            curr = prev
            prev = head
        #prev.next = curr
        #head = curr
        return None
    
    def printLL(self, head):
        # if(head == None):
        #     return 
        
        while(head != None):
            print(head.val)
            head = head.next
        
        
root = ListNode(1);
root.next = ListNode(2);
root.next.next = ListNode(3);
root.next.next.next = ListNode(4);

# while(root != None):
#     print(root.val)
#     root = root.next

sol = Solution()
root = sol.reverseList(root)

sol.printLL(root)


