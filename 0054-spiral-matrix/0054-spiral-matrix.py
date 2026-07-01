class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m, n = len(matrix), len(matrix[0])
        visited = [[False]*n for _ in range(m)]
        answer = []

        idx, cnt = 0, 0
        cur_r, cur_c = 0, 0

        print(f"row : {m} col : {n}")

        answer.append(matrix[cur_r][cur_c])
        visited[cur_r][cur_c] = True
        cnt += 1

        while cnt != m*n :
            while True :
                dr, dc = move[idx]
                new_r, new_c = cur_r + dr, cur_c + dc

                if 0<=new_r<m and 0<=new_c<n and not visited[new_r][new_c] :
                    cur_r, cur_c = new_r, new_c
                    break
                else :
                    idx = (idx + 1) % 4

            answer.append(matrix[cur_r][cur_c])
            visited[cur_r][cur_c] = True
            cnt += 1

        return answer
