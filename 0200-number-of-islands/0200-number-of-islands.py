class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rl, cl = len(grid), len(grid[0])
        visited = [[False]*cl for _ in range(rl)]

        from collections import deque
        answer = 0

        def adjacent(cur_r, cur_c) :
            dq = deque()
            dq.append([cur_r, cur_c])
            val = grid[cur_r][cur_c]
            visited[cur_r][cur_c] = True

            while dq :
                cur_r, cur_c = dq.popleft()
                for dr, dc in ([-1,0], [0,1], [1,0], [0,-1]) :
                    new_r, new_c = cur_r+dr, cur_c+dc
                    if 0<=new_r<rl and 0<=new_c<cl and not visited[new_r][new_c] and val == grid[new_r][new_c] :
                        visited[new_r][new_c] = True
                        dq.append([new_r, new_c])
            
            return 1

        for i in range(rl) :
            for j in range(cl) :
                if not visited[i][j] and grid[i][j] == "1" :
                    answer += adjacent(i, j)

        return answer