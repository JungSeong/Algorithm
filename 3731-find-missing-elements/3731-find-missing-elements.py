class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        answer = []

        for i in range(nums[0]+1, nums[-1]) :
            if i not in nums :
                answer.append(i)

        return answer