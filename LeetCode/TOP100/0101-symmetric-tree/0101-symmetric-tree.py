# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        from collections import deque

        if (not root.left and not root.right) :
            return True

        if (root.left and root.right) and root.left.val == root.right.val :
            dq = deque()
            dq.append([root.left, root.right])
        else :
            return False

        while dq :
            lst, rst = dq.popleft()

            if (lst.left and rst.right) :
                if (lst.left.val == rst.right.val) :
                    dq.append([lst.left, rst.right])
                else :
                    return False
            if (lst.right and rst.left) :
                if (lst.right.val == rst.left.val) :
                    dq.append([lst.right, rst.left]) 
                else :
                    return False

            if (not lst.left and rst.right) or (lst.left and not rst.right) or (lst.right and not rst.left) or (not lst.right and rst.left) :
                return False
        
        return True