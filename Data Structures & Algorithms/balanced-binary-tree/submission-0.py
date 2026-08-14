# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        switch = True
        if root is None:
            return True
        def height_tree(root):
            nonlocal switch

            if root is None:
                return 0

            left = height_tree(root.left)
            right = height_tree(root.right)

            if(abs(left-right)>1):
                switch = False
            return max(left,right)+1
        height_tree(root)
        return switch
        
        