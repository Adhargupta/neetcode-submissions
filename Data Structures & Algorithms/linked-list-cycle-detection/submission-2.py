# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = []
        current = head
        while current:
            if id(current) in arr:
                return True
            arr.append(id(current))
            current = current.next
        return False