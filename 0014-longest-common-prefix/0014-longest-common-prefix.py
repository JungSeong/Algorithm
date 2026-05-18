class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        ans = ""

        for ch in strs[0] :
            for st in strs :
                if not st.startswith(ans + ch) :
                    return ans
            ans += ch

        return ans