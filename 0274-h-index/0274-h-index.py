class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_val = citations[-1]

        from bisect import bisect_left
        answer = 0

        for i in range(max_val+1) :
            idx = bisect_left(citations, i)
            length = len(citations)-idx

            if length >= i :
                answer = max(answer, i)

        return answer