# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d = dict()
        cur = head

        while cur :
            if cur.val not in d.keys() :
                d[cur.val] = 1
            else :
                d[cur.val] += 1

            cur = cur.next
        
        dummy = ListNode(-1)
        c = dummy

        while head :
            if d[head.val] == 1 :
                c.next = ListNode(head.val)
                c = c.next
            head = head.next

        return dummy.next