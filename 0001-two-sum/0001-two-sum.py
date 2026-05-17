from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()
        for idx, n in enumerate(nums) :
            d[n] = idx

        for i in range(len(nums)) :
            if target-nums[i] in d.keys() and d[target-nums[i]] != i :
                return [i, d[target-nums[i]]]