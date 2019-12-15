class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Check the height
        def check(root):
            if root is None:
                return 0
            print(max(check(root.left), check(root.right)))
            return 1 + max(check(root.left), check(root.right))
        if root is None:
            return True
        return abs(check(root.left) - check(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        