class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        candidates = []
        
        for p in range(len(nums)-2) :
            if p>0 and nums[p] == nums[p-1] :
                continue

            left, right = p+1, len(nums)-1
            while left < right :
                if nums[left] + nums[right] + nums[p] == 0 :
                    candidates.append([nums[p], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1] :
                        left += 1
                    while left < right and nums[right] == nums[right-1] :
                        right -= 1

                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[p] :
                    left += 1 
                else :
                    right -= 1

        return candidates