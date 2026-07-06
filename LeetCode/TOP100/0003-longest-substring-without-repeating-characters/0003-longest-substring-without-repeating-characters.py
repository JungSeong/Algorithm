class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int :
        if len(s) == 0 :
            return 0
        dp = [1]*len(s)
        for i in range(1, len(s)) :
            d = []
            d.append(s[i])
            for j in range(i-1, -1, -1) :
                if s[j] not in d :
                    dp[i] += 1
                    d.append(s[j])
                else :
                    break

        return max(dp)