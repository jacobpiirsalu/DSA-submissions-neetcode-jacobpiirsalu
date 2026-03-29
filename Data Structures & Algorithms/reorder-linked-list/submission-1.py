# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
0->1->2->3->4->5->6

0->6


recursively: 
1. link first node to last node
2. recurse but with the prev first and last node excluded
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def recurse(head, length=1001): #ensure we travel to the end on the first iteration
            
            if length<=1:
                return head
            if length ==2: return head

            curr=head
            prev=None
            ctr=0
            while curr.next and ctr<length:
                prev=curr
                curr=curr.next
                ctr+=1
            
            prev.next=None
            tmp=head.next
            head.next = curr
            curr.next = tmp
            #tmp.next=None
            recurse(tmp, ctr-1)
            
            return head
        
        length=0
        curr=head
        while curr:
            curr=curr.next
            length+=1
        if length <=2:
            return
        recurse(head)
                
        