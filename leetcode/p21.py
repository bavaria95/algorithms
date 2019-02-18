# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            if not l1:
                return l2
            return l1

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        it = head

        while l1 or l2:
            if not l1:
                it.next = l2
                l2 = l2.next
            elif not l2:
                it.next = l1
                l1 = l1.next
            elif l1.val < l2.val:
                it.next = l1
                l1 = l1.next
            else:
                it.next = l2
                l2 = l2.next

            it = it.next
        
        return head
