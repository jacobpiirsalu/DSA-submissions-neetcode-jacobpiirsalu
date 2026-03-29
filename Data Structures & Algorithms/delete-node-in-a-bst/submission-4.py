# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def popInorderSuccessor(self, node: TreeNode) -> int:
        prev = None
        curr = node
        while curr.left:
            prev = curr
            curr = curr.left
        retVal = curr.val
        prev.left = None
        return retVal

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val == key:
            #delete this node
            # 0 children
            if not root.left and not root.right:
                return None
            # 1 child case
            elif root.left is None and root.right:
                return root.right
            elif root.right is None and root.left:
                return root.left
            # 2 children
            else:
                if root.right.left is None:
                    root.val = root.right.val
                    root.right = root.right.right
                else:
                    root.val = self.popInorderSuccessor(root.right)

            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        return root
                
        