class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = dict()
        for i in range(len(s)) :
            d[s[i]] = i

        print(d.items())

        st = []
        for i in range(len(s)) :
            if s[i] in st :
                continue
            else :
                while st and st[-1] > s[i] and i < d[st[-1]] :
                    st.pop()
                st.append(s[i])

        return "".join(st)