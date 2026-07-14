# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1, val2 = [], []

        while l1 :
            val1.append(l1.val)
            l1 = l1.next

        while l2 :
            val2.append(l2.val)
            l2 = l2.next
        
        num1 = int(("".join(map(str, val1)))[::-1])
        num2 = int(("".join(map(str, val2))[::-1]))
        num = str(num1 + num2)[::-1]

        cur = ListNode(-1)
        dummy = cur

        for n in num :
            dummy.next = ListNode(int(n))
            dummy = dummy.next

        return cur.next