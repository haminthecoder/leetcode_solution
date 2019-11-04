# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Preorder traversal => Doesn't cover edge case
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         s_pre = []
#         t_pre = []
#         def preorder(s: TreeNode, arr) -> None :
#             if s is not None:
#                 arr.append(s.val)
#             if s.left is not None:
#                 preorder(s.left, arr)
#             if s.right is not None:
#                 preorder(s.right, arr)
                
#         preorder(s, s_pre)
#         preorder(t, t_pre)
#         s_tree = "".join(str(e) for e in s_pre)
#         t_tree = "".join(str(e) for e in t_pre)
        
#         return t_tree in s_tree 
    
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSame(s, t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            if s.val != t.val:
                return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)
        if s is None:
            return False
        if isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
        

        
        
    
    
        
        