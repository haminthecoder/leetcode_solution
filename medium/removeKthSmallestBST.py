# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums = []
        self.inOrder(root, nums)
        return nums[k-1]
    
    def inOrder(self, root, nums):
        if root is None:
            return
        
        self.inOrder(root.left, nums)
        nums.append(root.val)
        self.inOrder(root.right, nums)
        
        return
                
        