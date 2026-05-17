from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr = sorted(arr)
        left, right = 0, len(nums)-1

        while left <= right :
            nl, nr = arr[left][0], arr[right][0]

            if nl + nr == target :
                return [arr[left][1], arr[right][1]]
            elif nl + nr > target :
                right -= 1
            else : 
                left += 1 