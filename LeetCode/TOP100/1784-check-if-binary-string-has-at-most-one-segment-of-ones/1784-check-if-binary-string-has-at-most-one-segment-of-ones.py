class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        zero = False
        for i in range(len(s)) :
            if zero and s[i] == "1" :
                return False
            if not zero and s[i] == "0" :
                zero = True
        return True