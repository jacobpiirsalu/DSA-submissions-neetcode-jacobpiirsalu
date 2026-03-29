# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEqual(self, root1, root2):
        if not root1 or not root2:
            return root1==root2
            
        return root1.val==root2.val and self.isEqual(root1.right, root2.right) and self.isEqual(root1.left, root2.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root==subRoot
        if self.isEqual(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)