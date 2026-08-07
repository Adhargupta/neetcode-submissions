# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current = list1
        current2 = list2
        arr = []

        while current is not None and current2 is not None:

            if current.val < current2.val:
                arr.append(current.val)
                current = current.next

            elif current.val > current2.val:
                arr.append(current2.val)
                current2 = current2.next

            else:
                arr.append(current.val)
                arr.append(current2.val)
                current = current.next
                current2 = current2.next

        while current is not None:
            arr.append(current.val)
            current = current.next

        while current2 is not None:
            arr.append(current2.val)
            current2 = current2.next

        # Convert array to linked list
        if not arr:
            return None

        head = ListNode(arr[0])
        temp = head

        for value in arr[1:]:
            temp.next = ListNode(value)
            temp = temp.next

        return head