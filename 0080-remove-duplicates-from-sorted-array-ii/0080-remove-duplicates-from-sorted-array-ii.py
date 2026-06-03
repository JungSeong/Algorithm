class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for n in nums :
            if write < 2 or nums[write-2] != n :
                nums[write] = n
                write += 1

        return write