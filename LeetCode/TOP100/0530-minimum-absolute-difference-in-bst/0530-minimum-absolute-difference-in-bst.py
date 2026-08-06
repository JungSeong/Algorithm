# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        possible = []
        answer = float('inf')

        from collections import deque
        dq = deque()
        if root :
            dq.append(root)

        while dq :
            Node = dq.popleft()
            possible.append(Node.val)

            if Node.left :
                dq.append(Node.left)
            if Node.right :
                dq.append(Node.right)
                
        for i in range(len(possible)) :
            for j in range(i+1, len(possible)) :
                answer = min(answer, abs(possible[i]-possible[j]))

        return answer