# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def right_view(root, level):
            if root is None:
                return

            # First node we encounter at this level
            if len(result) == level:
                result.append(root.val)

            # Visit right first
            right_view(root.right, level + 1)

            # Then visit left
            right_view(root.left, level + 1)

        right_view(root, 0)

        return result