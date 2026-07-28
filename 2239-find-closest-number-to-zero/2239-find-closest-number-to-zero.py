class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = -10**5-1

        for n in nums :
            if abs(ans) > abs(n) :
                ans = n
            if abs(ans) == abs(n) :
                ans = max(ans, n)

        return ans