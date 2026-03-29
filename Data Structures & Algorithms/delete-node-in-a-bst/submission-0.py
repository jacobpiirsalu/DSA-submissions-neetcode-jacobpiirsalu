# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinNode(self, root):
        curr = root
        while curr.left:
            curr = root.left
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: #node to delete
            # 2 children
            if root.left and root.right:
                minNode = self.getMinNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
            else: # 0 or 1 children
                return root.left if root.left else root.right
        return root


        