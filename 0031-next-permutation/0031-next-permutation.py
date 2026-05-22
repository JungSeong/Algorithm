class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        before = 0
        nonbreak = True
        for i in range(len(nums)-1, -1, -1) :
            if nums[i] < before : # 내림차순이 깨지는 순간
                idx = -1
                for j in range(len(nums)-1, i-1, -1) :
                    if nums[j] > nums[i] :
                        idx = j
                        break
                
                nums[i], nums[idx] = nums[idx], nums[i]
                print(nums)
                nn = nums[:i+1] + sorted(nums[i+1:])
                nums[:] = nn
                nonbreak = False
                break
            else :
                before = nums[i]
        
        if nonbreak :
            nums.reverse()