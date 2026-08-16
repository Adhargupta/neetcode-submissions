# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_value = root.val
        count = 0

        def good_node(root):
            nonlocal count, max_value

            if root is None:
                return

            old_max = max_value

            if root.val >= max_value:
                count += 1

            max_value = max(max_value, root.val)

            good_node(root.left)

            max_value = max(old_max, root.val)

            good_node(root.right)

            max_value = old_max

        good_node(root)

        return count