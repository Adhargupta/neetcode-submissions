# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy
        current = head

        while current:
            temp = current
            count = 0

            while temp and count < k:
                temp = temp.next
                count += 1

            if count < k:
                break

            # Save the first node of this group
            group_start = current

            # Reverse k nodes
            prev = None

            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Connect group
            group_prev.next = prev
            group_start.next = current

            # Move to the end of reversed group
            group_prev = group_start

        return dummy.next