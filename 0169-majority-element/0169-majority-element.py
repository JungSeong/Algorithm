class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        length = len(nums)//2

        cnt = Counter(nums)

        for k, v in cnt.items() :
            if v > length :
                return k