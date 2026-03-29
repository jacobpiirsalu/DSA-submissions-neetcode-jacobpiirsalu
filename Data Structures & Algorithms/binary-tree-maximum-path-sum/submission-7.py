class Solution:
    def maxPath(self, root):
        if not root: return 0
        left = max(0, self.maxPath(root.left))
        right = max(0, self.maxPath(root.right))
        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return -float('inf')
        return max(root.val + max(0, self.maxPath(root.left)) + max(0, self.maxPath(root.right)),
        self.maxPathSum(root.left), self.maxPathSum(root.right))