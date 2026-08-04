# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        d = dict()
        turn = dict()
        idx = 1

        while head :
            d[idx] = head.val
            idx += 1
            head = head.next
            
        for i in range(1, idx) :
            if left <= i <= right :
                turn[i] = right-i+left
            else :
                turn[i] = i

        dummy = ListNode(-1)
        cur = dummy

        for i in range(1, idx) :
            cur.next = ListNode(d[turn[i]])
            cur = cur.next

        return dummy.next