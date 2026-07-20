class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        cgrid = [[0]*n for _ in range(m)]

        for i in range(k) :
            for r in range(m) :
                for c in range(n):
                    if r != m-1 and c == n-1 :
                        cgrid[r+1][0] = grid[r][c]
                    elif r == m-1 and c == n-1 :
                        cgrid[0][0] = grid[r][c]
                    else :
                        cgrid[r][c+1] = grid[r][c]
            
            for i in range(m) :
                grid[i][:] = cgrid[i][:]

        return grid
                    