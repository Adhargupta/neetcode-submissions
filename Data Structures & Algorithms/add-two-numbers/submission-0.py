# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []

        # Convert l1 to array
        current = l1
        while current:
            arr1.append(current.val)
            current = current.next

        # Convert l2 to array
        current2 = l2
        while current2:
            arr2.append(current2.val)
            current2 = current2.next

        # Add arrays
        arr3 = []
        carry = 0
        i = 0

        while i < len(arr1) or i < len(arr2) or carry:

            val1 = arr1[i] if i < len(arr1) else 0
            val2 = arr2[i] if i < len(arr2) else 0

            total = val1 + val2 + carry

            arr3.append(total % 10)
            carry = total // 10

            i += 1

        # Convert result array to linked list
        if not arr3:
            return None

        new_head = ListNode(arr3[0])
        current3 = new_head

        for i in range(1, len(arr3)):
            current3.next = ListNode(arr3[i])
            current3 = current3.next

        return new_head