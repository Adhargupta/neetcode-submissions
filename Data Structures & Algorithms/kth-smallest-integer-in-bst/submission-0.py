# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def valueOfTree(root):
            if(root is None):
                return
            arr.append(root.val)
            left = valueOfTree(root.left)
            right = valueOfTree(root.right)
        valueOfTree(root)
        arr.sort()
        return arr[k-1]