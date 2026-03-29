# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSumV2(self, root, currSum, targetSum):
        
        if not root:
            return False
        currSum += root.val
        if not root.right and not root.left:
            return currSum == targetSum
        
        return self.hasPathSumV2(root.left, currSum, targetSum) or self.hasPathSumV2(root.right, currSum, targetSum) 

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumV2(root, 0, targetSum)

        