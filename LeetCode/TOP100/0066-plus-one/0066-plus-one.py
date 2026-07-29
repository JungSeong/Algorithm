class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i_digit = int("".join(map(str, digits))) + 1
        answer = []

        for ch in str(i_digit) :
            answer.append(int(ch))

        return answer