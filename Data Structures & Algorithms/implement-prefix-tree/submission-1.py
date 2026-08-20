class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = Node()
            current_node = current_node.children[ch]
        current_node.is_end = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                return False
            current_node = current_node.children[ch]
        return current_node.is_end

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for ch in prefix:
            if ch not in current_node.children:
                return False
            current_node = current_node.children[ch]
        return True
        