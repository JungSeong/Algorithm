class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        return bisect_left(nums, target)