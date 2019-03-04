# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return None

        num = 0
        p = head
        while p:
            num += 1
            p = p.next

        p1 = head
        p2 = head

        for _ in range(k % num):
            if p1:
                p1 = p1.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = head
        head = p2.next
        p2.next = None

        return head
