# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, lst):
        if not root:
            return
        self.inorder(root.left,lst)
        lst.append(root.val)
        self.inorder(root.right,lst)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.inorder(root, lst)
        return lst
        