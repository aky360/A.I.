class SLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
root = SLinkedList(1)
root1 = SLinkedList(2)
root2 = SLinkedList(3)
root3 = SLinkedList(4)
root4 = SLinkedList(5)
root.next = root1
root1.next = root2
root2.next = root3
root3.next = root4
root4.next = None


"""another way to creating the linked list is"""

head = SLinkedList(5)
head.next = SLinkedList(6)
head.next.next = SLinkedList(7)
head.next.next.next = SLinkedList(8)
    
def printLList(head):
    if not head or not head.next:
        return head
    else:
        while head!=None:
            print('data ' ,head.data)
            head = head.next
    
"""
Reverse a singly linked list. For example:
1 --> 2 --> 3 --> 4
After reverse:
4 --> 3 --> 2 --> 1
"""

def rev_LList(head):
    if not head or not head.next:
        return head
        
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev    
        
print('before reverse data ')
print(printLList(head))
rev = rev_LList(head)
print('after reverse list data ')
print(printLList(rev))


# ===================================================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    sol = Solution()
    print(sol.reverseList(head))
    print(sol.reverseList(head).val)
