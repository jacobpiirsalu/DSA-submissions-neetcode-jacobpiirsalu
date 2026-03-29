# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafPathSum(self, root: Optional[TreeNode], path: List[int], targetSum: int) -> bool:
        if not root:
            return False
        path.append(root.val)
        if self.leafPathSum(root.left, path, targetSum):
            return True
        if self.leafPathSum(root.right, path, targetSum):
            return True
        if not root.right and not root.left:
            if sum(path) == targetSum:
                return True
        path.pop()
        return False
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        return self.leafPathSum(root, path, targetSum)
        