# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [root]
        
        while queue:
            xExists, yExists = False, False
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.val is x:
                    xExists = True
                if curr.val is y:
                    yExists = True
                if curr.left and curr.right:
                    if curr.left.val == x and curr.right.val == y :
                        return False
                    if curr.left.val == y and curr.right.val == x :
                        return False
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if xExists and yExists:
                return True
        return False
        