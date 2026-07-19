class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rx, cx = 0, x
        mul = 1

        while cx // 10 > 0 :
            mul *= 10
            cx //= 10

        cx = x

        while cx > 0 :
            rx += (cx%10)*mul
            mul //= 10
            cx //= 10

        if x == rx :
            return True
        return False   