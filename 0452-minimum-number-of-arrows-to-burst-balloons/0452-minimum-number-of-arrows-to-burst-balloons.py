class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        points.append([float('inf'), float('inf')])
        print(points)
        answer = 0
        i = 0
        
        while True :
            if i >= len(points)-1 :
                break
            pos = points[i][1]
            t = i

            while t+1 < len(points) and points[t+1][0] <= pos :
                t += 1
                pos = min(pos, points[t][1])

            answer += 1
            i = t+1
        
        return answer