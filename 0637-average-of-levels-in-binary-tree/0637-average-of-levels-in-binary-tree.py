# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        answer = []

        dq = deque()
        dq.append(root)
        answer.append(root.val)

        while dq :
            leaf_nodes = []
            while dq :
                node = dq.popleft()
                
                if node.left :
                    leaf_nodes.append(node.left)
                if node.right :
                    leaf_nodes.append(node.right)

            avg = 0
            for i in range(len(leaf_nodes)) :
                avg += leaf_nodes[i].val
            
            if leaf_nodes :
                answer.append(avg/len(leaf_nodes))
                dq.extend(leaf_nodes)

        return answer