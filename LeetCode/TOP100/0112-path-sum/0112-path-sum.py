# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque

        dq = deque()
        if root :
            dq.append([root, root.val])

        while dq :
            node, cur = dq.popleft()

            if not node.left and not node.right and cur == targetSum :
                return True
            
            if node.left :
                dq.append([node.left, cur + node.left.val])
            if node.right :
                dq.append([node.right, cur + node.right.val])
        
        return False