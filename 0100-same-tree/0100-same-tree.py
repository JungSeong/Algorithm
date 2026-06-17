# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        else :
            from collections import deque
            dq = deque()
            dq.append([p, q])

            while dq :
                cur_p, cur_q = dq.popleft()

                if cur_p and cur_q :
                    if cur_p.val != cur_q.val :
                        return False
                    else :
                        dq.append([cur_p.left, cur_q.left])
                        dq.append([cur_p.right, cur_q.right])
                elif cur_p and cur_q==None or cur_p==None and cur_q :
                    return False

            return True