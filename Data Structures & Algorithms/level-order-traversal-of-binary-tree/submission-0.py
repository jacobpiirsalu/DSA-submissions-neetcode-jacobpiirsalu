# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        retLst = []
        q = deque()
        q.append(root)
        
        

        while q:
            nodes = []
            while q:
                nodes.append(q.popleft())
            print([n.val for n in nodes])
            retLst.append([n.val for n in nodes])
            for n in nodes:
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
        
        return retLst
        
            
            

        