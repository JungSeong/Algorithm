class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0

        nums = sorted(set(nums))
        answer = 0
        cur = 1

        for i in range(1, len(nums)) :
            if nums[i] == nums[i-1]+1 :
                cur += 1
            else :
                answer = max(answer, cur)
                cur = 1

        answer = max(answer, cur)
        
        return answer