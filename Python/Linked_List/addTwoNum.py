# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1 
        n2 = l2
        fakeHead = ListNode(None)
        result = fakeHead
        toAdd = 0
        while(!(n1 == None and n2 == None)):
            v1 = 0
            v2 = 0
            if(n1!=None):
                v1 = n1.val
                n1 = n1.next
            if(n2 != None):
                v2 = n2.val
                n2 = n2.next
            tmp = v1 + v2 +toAdd
            result.next = ListNode(tmp%10)
            result = result.next
            toAdd = tmp/10
            
        if(toAdd>0):
            result.next = ListNode(toAdd)
        
        return fakeHead.next
