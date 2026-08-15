# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(root1, root2):
            switch = True

            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None:
                return False

            if root1.val != root2.val:
                return False

            left = isSame(root1.left, root2.left)
            right = isSame(root1.right, root2.right)

            if left == False or right == False:
                switch = False

            return switch

        def height_tree(root):
            if root is None:
                return False

            if root.val == subRoot.val:
                if isSame(root, subRoot):
                    return True

            left = height_tree(root.left)
            right = height_tree(root.right)

            if left == True or right == True:
                return True

            return False

        return height_tree(root)
            