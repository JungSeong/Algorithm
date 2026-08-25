# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        from collections import deque

        def height(node: Optional[TreeNode]) -> int :
            if not node :
                return 0
            return 1 + max(height(node.left), height(node.right))

        dq = deque()
        if not root :
            return True
        else :
            dq.append(root)

        while dq :
            Node = dq.popleft()

            if abs(height(Node.left)-height(Node.right))>1 :
                return False
            
            if Node.left :
                dq.append(Node.left)
            if Node.right :
                dq.append(Node.right)

        return True