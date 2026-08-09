# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for list_item in lists:
            current = list_item

            while current:
                arr.append(current.val)
                current = current.next

        # Handles lists = [] and lists = [[]]
        if not arr:
            return None

        arr.sort()

        head = ListNode(arr[0])
        current2 = head

        for i in range(1, len(arr)):
            current2.next = ListNode(arr[i])
            current2 = current2.next

        return head