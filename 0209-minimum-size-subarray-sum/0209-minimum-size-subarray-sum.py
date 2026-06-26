class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cum_arr = []
        cum_arr.append(0)
        answer = float('inf')

        for i in range(len(nums)) :
            cum_arr.append(cum_arr[-1] + nums[i])

        if cum_arr[-1] < target :
            return 0

        from bisect import bisect_left

        for i in range(len(nums)) :
            idx = bisect_left(cum_arr, target + cum_arr[i], i+1)

            if idx <= len(nums) :
                answer = min(answer, idx-i)

        return answer