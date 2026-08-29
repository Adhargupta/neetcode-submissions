# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(result)

    def deserialize(self, data):
        values = iter(data.split(","))

        def dfs():
            val = next(values)

            if val == "N":
                return None

            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
