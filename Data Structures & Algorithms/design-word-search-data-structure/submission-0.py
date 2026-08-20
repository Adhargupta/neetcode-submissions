class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current_node = self.root

        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = Node()

            current_node = current_node.children[ch]

        current_node.is_end = True

    def search(self, word: str) -> bool:

        def check(node, index):

            if index == len(word):
                return node.is_end

            ch = word[index]

            if ch == '.':
                for child in node.children.values():
                    if check(child, index + 1):
                        return True
                return False

            if ch not in node.children:
                return False

            return check(node.children[ch], index + 1)

        return check(self.root, 0)