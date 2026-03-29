# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        tops = []
        for i,head in enumerate(lists):
            tops.append((head.val, i, head))
        heapq.heapify(tops)
        
        head = tops[0]
        
        while len(tops)>1:
            tmp = tops[0]
            heapq.heappop(tops)
            if tmp[2].next:
                heapq.heappush(tops,(tmp[2].next.val, tmp[1], tmp[2].next))
            
            tmp[2].next = tops[0][2]
        
        
        return head[2]

        