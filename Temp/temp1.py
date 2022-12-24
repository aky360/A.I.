# 24/12/22 #

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class ListRev:
    def revLList(self, l: ListNode) -> ListNode:
        prev = None
        curr = l
        while(curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = curr.next
        
        l = prev
        
        while(prev != None):
            print(prev.val, end=" ")
            prev = prev.next
        return prev
        
    def printList(self, l: ListNode):
        temp = l
        while(temp != None):
            print(temp.val, end=" ")
            temp = temp.next
        
        

llist = ListNode(10)
llist.next  = ListNode(20)
llist.next.next = ListNode(30)
llist.next.next.next = ListNode(40)
llist.next.next.next.next=ListNode(50)
llist.next.next.next.next.next = None

# while(llist):
#     print(llist.val)
#     llist = llist.next

sol = ListRev()
sol.revLList(llist)
#sol.printList(sol.revLList(llist))
        
