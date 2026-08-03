"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        origin = head

        d = {}

        while head :
            d[head] = Node(head.val)
            head = head.next       

        head = origin 

        while head :
            if head.next :
                d[head].next = d[head.next]
            if head.random :
                d[head].random = d[head.random]
            head = head.next

        head = origin

        if not head :
            return None

        return d[origin]