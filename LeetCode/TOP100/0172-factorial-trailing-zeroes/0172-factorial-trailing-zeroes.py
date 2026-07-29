class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0

        for i in range(1, n+1) :
            while not i % 5 :
                ans += 1
                i //= 5
        
        return ans