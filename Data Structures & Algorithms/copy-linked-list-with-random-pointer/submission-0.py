"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        
        # Store original nodes
        arr = []
        current = head

        while current:
            arr.append(current)
            current = current.next

        # Map original node → copied node
        copies = {}

        for node in arr:
            copies[node] = Node(node.val)

        # Connect next and random
        for node in arr:
            copies[node].next = copies.get(node.next)
            copies[node].random = copies.get(node.random)

        # Return copied head
        return copies.get(head)