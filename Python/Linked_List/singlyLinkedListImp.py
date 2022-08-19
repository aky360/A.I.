class SLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
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


"""
Given a list, rotate the list to the right by k places,
where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

def rotate_List(head):
    if not head or not head.next:
        return head
    
    curr = head
    temp = head
    head = head.next
    while curr.next:
        curr=curr.next
    curr.next = temp
    temp.next = None
    return head
    
def rotate_K_Times(head, k):
    for i in range(k):
        head = rotate_List(head)
    return head
    
rotate = rotate_K_Times(head, 1)
print(printLList(rotate))
