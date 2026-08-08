# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        desired_length = count - n

        if desired_length == 0:
            return head.next

        count2 = 0
        current = head
        prev = None

        while current is not None:
            count2 += 1

            if count2 == desired_length:
                current.next = current.next.next
                break

            prev = current
            current = current.next

        return head
