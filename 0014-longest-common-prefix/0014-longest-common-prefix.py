class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        strs.sort(key = len)
        
        for ch in strs[0] :
            for st in strs :
                if not st.startswith(lcp + ch) :
                    return lcp
            lcp += ch
        return lcp