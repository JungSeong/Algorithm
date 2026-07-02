class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left, right = 0, 0
        nums.append(-float('inf'))
        answer = []

        for i in range(1, len(nums)) :
            if nums[i] == nums[i-1]+1 :
                right += 1
            else :
                if left-right == 0 :
                    answer.append(str(nums[left]))
                else :
                    answer.append(f"{nums[left]}->{nums[right]}")
                left, right = i, i
        
        return answer