class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        left, right = 1, 1

        for i in range(1, len(nums)) :
            left *= nums[i-1]
            answer[i] *= left
        
        for i in range(len(nums)-2, -1, -1) :
            right *= nums[i+1]
            answer[i] *= right

        return answer