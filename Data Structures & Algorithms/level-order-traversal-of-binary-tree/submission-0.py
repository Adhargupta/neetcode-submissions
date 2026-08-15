# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        arr = []

        def sub_list(root, level):
            if root is None:
                return

            if len(arr) == level:
                arr.append([])

            arr[level].append(root.val)

            sub_list(root.left, level + 1)
            sub_list(root.right, level + 1)

        sub_list(root, 0)

        return arr