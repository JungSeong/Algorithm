# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque

        def BFS() :
            dq = deque()
            if root :
                dq.append(root)

            while dq :
                Node = dq.popleft()

                if Node.left or Node.right :
                    Node.left, Node.right = Node.right, Node.left

                    if Node.left :
                        dq.append(Node.left)
                    if Node.right :
                        dq.append(Node.right)
        
        BFS()
        return root