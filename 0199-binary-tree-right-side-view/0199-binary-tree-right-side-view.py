# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        answer = []
        dq = deque()
        if root :
            dq.append(root)
            answer.append(root.val)

        while dq :
            st = []
            additional = []
            while dq :
                Node = dq.popleft()

                if Node.left :
                    st.append(Node.left)
                    additional.append(Node.left)
                if Node.right :
                    st.append(Node.right)
                    additional.append(Node.right)

            if st :
                right_node = st.pop()
                answer.append(right_node.val)
            dq.extend(additional)
            print(dq)

        return answer