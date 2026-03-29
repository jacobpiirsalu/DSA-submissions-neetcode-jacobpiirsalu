# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, h1: ListNode, h2: ListNode):
        dummy = ListNode()
        curr = dummy
        while h1 and h2:
            if h1.val <= h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
        if h1:
            curr.next = h1
        elif h2:
            curr.next = h2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or not lists[0]:
            return None
        while len(lists)>1:
            mergedLsts = []
            for i in range(0, len(lists),2):
                mergedLsts.append(self.mergeTwoLists(lists[i], lists[i+1] if i+1 < len(lists) else None))

            lists=mergedLsts
        return lists[0]
        
