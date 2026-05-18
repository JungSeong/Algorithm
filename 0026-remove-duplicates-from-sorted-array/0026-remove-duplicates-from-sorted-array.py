class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        nums[:] = sorted(s)
        return len(nums)