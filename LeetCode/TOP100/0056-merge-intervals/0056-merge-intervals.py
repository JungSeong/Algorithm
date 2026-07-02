class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervals.append([-1, -1])
        answer = []
        isIN = False

        for i in range(1, len(intervals)) :
            si, ei = intervals[i][0], intervals[i][1]
            sb, eb = intervals[i-1][0], intervals[i-1][1]
            if 0 <= si <= eb :
                if 0 <= ei <= eb : # 전부 안에 들어간 경우
                    intervals[i][0], intervals[i][1] = intervals[i-1][0], intervals[i-1][1]
                else : # 왼쪽만 안에 들어간 경우
                    intervals[i][0], intervals[i][1] = intervals[i-1][0], intervals[i][1]
            else :
                answer.append([sb, eb])

        return answer