# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        unique_head = head
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return unique_head
