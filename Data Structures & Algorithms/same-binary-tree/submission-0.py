# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        switch = True

        def check(root1, root2):
            nonlocal switch

            if root1 is None and root2 is None:
                return

            if root1 is None or root2 is None:
                switch = False
                return

            if root1.val != root2.val:
                switch = False
                return

            check(root1.left, root2.left)
            check(root1.right, root2.right)

        check(p, q)

        return switch