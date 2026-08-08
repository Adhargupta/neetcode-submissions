# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodes = []
        current = head

        # Store the actual nodes
        while current:
            nodes.append(current)
            current = current.next

        left = 0
        right = len(nodes) - 1

        # Reconnect nodes: 0, n-1, 1, n-2, ...
        while left < right:

            nodes[left].next = nodes[right]
            left += 1

            nodes[right].next = nodes[left]
            right -= 1

        # End the list
        nodes[left].next = None
