# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        dq = deque()
        if not root :
            return 0

        dq.append([root, 1])
        answer = 1

        while dq :
            node, depth = dq.popleft()
            answer = max(answer, depth)

            if node.left :
                dq.append([node.left, depth+1])
            if node.right :
                dq.append([node.right, depth+1])

        return answer