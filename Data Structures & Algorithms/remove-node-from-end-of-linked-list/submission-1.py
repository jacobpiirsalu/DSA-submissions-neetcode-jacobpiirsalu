# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #edge cases:
        # head is none -> not an option
        #list length is 1
        #n is not actually a valid idx to remove ->not an option
        if not head:
            return None


        length=0
        curr=head
        while curr:
            curr=curr.next
            length+=1
        if length==n: return head.next
        curr=head
        prev=None
        for i in range(length-n):
            prev=curr
            curr=curr.next
        
        prev.next = curr.next
        curr.next=None
        return head
            
