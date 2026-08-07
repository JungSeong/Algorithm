# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        cur = head
        before, after = [], []

        while cur :
            if cur.val < x :
                before.append(ListNode(cur.val))
            else :
                after.append(ListNode(cur.val))

            cur = cur.next

        dummy = ListNode(-1)
        cur = dummy

        for Node in before :
            cur.next = Node
            cur = cur.next

        for Node in after :
            cur.next = Node
            cur = cur.next

        return dummy.next