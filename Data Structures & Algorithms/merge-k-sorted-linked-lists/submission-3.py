# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        tops = []
        for head in lists:
            tops.append(head)
        
        tops.sort(key= lambda x: x.val)
        head = tops[0]
        
        while len(tops)>1:
            tops.sort(key= lambda x: x.val)
            tmp = tops[0]
            del tops[0]
            if tmp.next:
                tops.append(tmp.next)
            tops.sort(key= lambda x: x.val)
            tmp.next = tops[0]
        
        
        return head

        