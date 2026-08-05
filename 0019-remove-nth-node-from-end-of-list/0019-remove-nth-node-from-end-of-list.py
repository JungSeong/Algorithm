# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        d = dict()
        idx = 0

        while head :
            d[idx] = head
            head = head.next
            idx += 1

        dummy = ListNode(-1)
        cur = dummy

        for i in range(idx) :
            if i != idx-n :
                cur.next = d[i]
                cur = cur.next

        cur.next = None
        
        return dummy.next