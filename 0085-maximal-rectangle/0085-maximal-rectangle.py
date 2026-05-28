class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        h, w = len(matrix), len(matrix[0])
        heights = [0]*w
        best_area = 0

        for r in range(h) :
            for c in range(w) :
                if matrix[r][c] == "1" :
                    heights[c] += 1
                else :
                    heights[c] = 0
        
            stack = [] # (start_col, height)

            for c in range(w+1) :
                cur_height = heights[c] if c < w else 0
                start = c

                while stack and stack[-1][1] > cur_height : # 이전 막대의 높이가 지금 들어올 높이보다 높다면
                    prev_start, height = stack.pop()
                    best_area = max(best_area, height * (c-prev_start)) # 이전 막대까지의 높이를 최대 area로 우선 설정
                    start = prev_start # start를 이전 막대의 행 번호로 설정

                stack.append((start, cur_height))

        return best_area