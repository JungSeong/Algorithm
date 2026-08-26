class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        K = k
        start, end = 0, 0
        answer = 0
        
        from collections import deque
        dq = deque()

        for i in range(len(nums)) :
            if nums[i] : # 1
                end += 1
            else : # 0
                if K : # >= 1
                    K -= 1
                    end += 1
                    dq.append(i)
                else :
                    answer = max(answer, end-start)
                    if k != 0 :
                        idx = dq.popleft()
                        start = idx+1
                        dq.append(i)
                        end += 1
                    else :
                        start, end = i+1, i+1
        
        answer = max(answer, end-start)

        return answer