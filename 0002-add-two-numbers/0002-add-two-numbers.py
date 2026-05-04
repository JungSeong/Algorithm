# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur = ListNode(-1)
        dummy = cur

        while l1 or l2 or carry :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            num = val % 10

            dummy.next = ListNode(num)
            dummy = dummy.next

            if l1 :
                l1 = l1.next
            if l2 :
                l2 = l2.next

        return cur.next