# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfsSum(node, ssum) -> bool:
            if not node: return False
            ssum += node.val
            if not node.left and not node.right:
                return ssum == targetSum
            return dfsSum(node.left, ssum) or dfsSum(node.right, ssum)

        return dfsSum(root, 0)

        
