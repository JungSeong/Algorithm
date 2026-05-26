class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        from bisect import bisect_left, bisect_right
        if not nums :
            return [-1, -1]
    
        bl, br = bisect_left(nums, target), bisect_right(nums, target)-1
        bl = bl if 0<=bl<len(nums) and nums[bl] == target else -1
        br = br if 0<=bl<len(nums) and nums[br] == target else -1
        
        return [bl, br]