# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        sum_head = ListNode('+')
        l3 = sum_head
        s = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            s = l1_val + l2_val + s
            l3.next = ListNode(s % 10)
            l3 = l3.next

            s //= 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if s:
            l3.next = ListNode(s)

        return sum_head.next
