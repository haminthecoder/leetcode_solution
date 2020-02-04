# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        stack = []
        stack.append(root)
        while stack:
            currentNode = stack.pop()
            left = currentNode.left
            currentNode.left = currentNode.right
            currentNode.right = left
            
            if currentNode.left:
                stack.append(currentNode.left)
            
            if currentNode.right:
                stack.append(currentNode.right)
        return root
            
        