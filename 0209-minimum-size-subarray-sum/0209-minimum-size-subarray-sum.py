class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        cum = nums[left]
        answer = float('inf')

        if (sum(nums) < target) :
            return 0

        while True :
            if cum < target :
                if right+1 >= len(nums) :
                    break
                else :
                    right += 1
                    cum += nums[right]
            else :
                answer = min(answer, right-left+1)
                cum -= nums[left]
                left += 1

        return answer