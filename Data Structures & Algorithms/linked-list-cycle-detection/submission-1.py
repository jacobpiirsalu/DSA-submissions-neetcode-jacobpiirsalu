# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        
        visited = set()
        curr = head
        while curr.next:
            if (curr.val, curr.next.val) in visited:
                return True
            else:
                visited.add((curr.val, curr.next.val))
            curr = curr.next
        return False
