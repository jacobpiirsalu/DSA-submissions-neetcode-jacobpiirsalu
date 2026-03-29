# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorderLst = []
        def inorder(node):
            if node is None:
                return node
            if len(inorderLst) == k:
                return
            inorder(node.left)
            inorderLst.append(node.val)
            if len(inorderLst) == k:
                return
            inorder(node.right)
        
        inorder(root)
        return inorderLst[k-1]
        