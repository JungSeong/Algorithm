class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        answer = [[0]*n for _ in range(m)]

        def rules(cur_r, cur_c) :
            loc = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
            alive, death = 0, 0

            for dr, dc in loc :
                new_r, new_c = cur_r + dr, cur_c + dc 
                if 0<=new_r<m and 0<=new_c<n :
                    if board[new_r][new_c] :
                        alive += 1
                    else :
                        death += 1

            print(f"{alive} {death}")

            if board[cur_r][cur_c] and alive < 2 :
                return 0
            if board[cur_r][cur_c] and 2<=alive<=3 :
                return 1
            if board[cur_r][cur_c] and alive > 3 :
                return 0
            if not board[cur_r][cur_c] and alive == 3 :
                return 1
            
            return board[cur_r][cur_c]

        for i in range(m) :
            for j in range(n) :
                answer[i][j] = rules(i, j)

        for i in range(m) :
            board[i][:] = answer[i][:]