# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        validRange = (-float('inf'), float('inf'))
        def isValid(node, validRange):
            
            if not node:
                return True

            #2 children
            if validRange[0] < node.val < validRange[1]:
                return isValid(node.left, (validRange[0], node.val)) and isValid(node.right, (node.val, validRange[1]))
            return False
        return isValid(root, validRange)

        