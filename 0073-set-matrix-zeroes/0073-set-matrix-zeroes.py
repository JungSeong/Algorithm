class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeros = []

        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    zeros.append((i, j))

        print(zeros)

        for i, j in zeros :
            left, right, up, down = j, j, i, i

            while left != 0 or right != n-1 or up != 0 or down != m-1  :
                if 0 <= left-1 :
                    left -= 1
                if right+1 < n :
                    right += 1
                if 0<=up-1 :
                    up -= 1
                if down+1 < m :
                    down += 1
                
                matrix[i][left] = 0
                matrix[i][right] = 0
                matrix[up][j] = 0
                matrix[down][j] = 0