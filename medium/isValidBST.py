class Solution:
    # Checking BST
    def check_bst(self, root, lo, hi):
        if root is None:
            return True
        if not lo < root.val < hi:
            return False
        return self.check_bst(root.left, lo, min(hi, root.val)) and self.check_bst(root.right, max(lo, root.val), hi)
    
    def isValidBST(self, root):
        return self.check_bst(root, float("-inf"), float("inf"))