# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        cur = head
        cnt = 0
        idx = k

        while cur :
            cnt += 1
            cur = cur.next

        d = dict()

        while head :
            d[idx % cnt] = ListNode(head.val)
            idx += 1
            head = head.next
        
        dummy = ListNode(-1)
        cur = dummy

        for i in range(cnt) :
            cur.next = d[i]
            cur = cur.next

        return dummy.next