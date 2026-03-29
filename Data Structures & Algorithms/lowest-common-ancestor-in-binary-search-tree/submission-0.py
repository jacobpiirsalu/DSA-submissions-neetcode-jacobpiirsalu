# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = []
        q_path = []


        def binSearch(node, target, path):
            path.append(node)
            if node.val == target.val:
                return
            else:
                if target.val < node.val:
                    binSearch(node.left, target, path)
                else:
                    binSearch(node.right, target, path)
        
        binSearch(root, p, p_path)
        binSearch(root, q, q_path)

        while len(p_path) > len(q_path):
            p_path.pop()
        while len(p_path) < len(q_path):
            q_path.pop()

        while p_path[-1] != q_path[-1]:
            p_path.pop()
            q_path.pop()
        return p_path[-1]


