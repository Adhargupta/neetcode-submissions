class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):

        # Build Trie
        root = TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        result = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node):

            # Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Already visited
            if board[r][c] == "#":
                return

            char = board[r][c]

            # Character doesn't exist in Trie
            if char not in node.children:
                return

            node = node.children[char]

            # Complete word found
            if node.word:
                result.append(node.word)
                node.word = None   # prevent duplicate

            # Mark visited
            board[r][c] = "#"

            # Explore 4 directions
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            # Backtrack
            board[r][c] = char

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result