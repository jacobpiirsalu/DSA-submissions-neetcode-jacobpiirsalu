# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, n1:ListNode, n2:ListNode) -> Optional[ListNode]:
        #lists is guaranteed to combining 2 linked lists [1->3->9]+[2->4->6]
        dummy = ListNode()
        curr = dummy
        while n1 and n2:
            if n1.val <= n2.val:
                curr.next = n1
                n1 = n1.next
            else:
                curr.next = n2
                n2 = n2.next
            curr = curr.next
        
        while n1:
            curr.next = n1
            n1 = n1.next
            curr = curr.next
        while n2:
            curr.next = n2
            n2 = n2.next
            curr = curr.next
        return dummy.next
        


    # def mergeAllLists(self, lists: List[Optional[ListNode]], s:int, e:int) -> Optional[ListNode]:
    #     #base cases:
    #     #A) merge 2 lists
    #     #B) merge 1 or 0 lists

    #     if e-s <= -1:
    #         return lists
    #     if e-s==0:
    #         return lists[0]
    #     #merge 2 lists: like mergesort
        

    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: 
            return None
        if len(lists) == 1: 
            return lists[0]

        while len(lists) > 1:
            lists[0] = self.mergeTwoLists(lists[0], lists[1])
            lists.pop(1)

        return lists[0]
        
        