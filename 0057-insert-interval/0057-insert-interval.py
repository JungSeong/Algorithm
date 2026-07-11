class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        answer = []

        if len(intervals) == 0 :
            return [newInterval]

        intervals.append([float('inf'), float('inf')])
        sn, en = newInterval[0], newInterval[1]
        idx = 0
        
        for si, ei in intervals :
            if ei < sn : # 아애 해당 구간 오른쪽에 있는 경우
                answer.append([si, ei])
            elif si <= sn <= ei and ei < en : # 왼쪽 일부가 곂치는 경우
                print("test1")
                intervals[idx][0], intervals[idx][1] = si, en
                sn, en = si, en
            elif si <= sn <= ei and en <= ei : # 아애 해당 범위 내에 들어가는 경우
                answer.append([si, ei])
                idx += 1
                break
            elif sn <= si and ei <= en : # 현재 interval이 해당 범위 내에 들어가는 경우
                intervals[idx][0], intervals[idx][1] = sn, en
            elif sn < si and si <= en <= ei : # 오른쪽 일부가 곂치는 경우
                intervals[idx][0], intervals[idx][1] = sn, ei
                sn, en = sn, ei
            elif en < si : # 위의 Case에 해당하지 않으면서 왔고, 아애 해당 구간 왼쪽에 있는 경우
                answer.append([sn, en])
                break
            idx += 1

        if idx < len(intervals) :
            for i in range(idx, len(intervals)-1) :
                answer.append(intervals[i])

        return answer