class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int :
        left, right = 0, 0
        max_len = 0
        d = set()
        if len(s) == 0 :
            return 0

        for i in range(len(s)) :
            if not d :
                d.add(s[i])
                max_len = max(max_len, 1)
            else :
                if s[i] not in d :
                    d.add(s[i])
                    right += 1
                    max_len = max(max_len, right-left+1)
                else :
                    for j in range(i-1, -1, -1) :
                        if s[j] == s[i] :
                            break
                    left, right = j+1, i
                    d = set()
                    for p in range(left, i+1) :
                        d.add(s[p])

        max_len = max(max_len, right-left+1)

        print(max_len)
        return max_len