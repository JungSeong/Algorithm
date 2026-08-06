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
        stack = []
        cur = root
        prev = None
        ans = float('inf')

        while cur or stack :
            while cur :
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if prev is not None :
                ans = min(ans, cur.val - prev)
            prev = cur.val
            cur = cur.right

        return ans