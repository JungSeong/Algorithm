class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        if min(len(word1), len(word2)) == len(word1) :
            for i in range(len(word1)) :
                ans += word1[i]
                ans += word2[i]
            ans += word2[len(word1):]
        else :
            for i in range(len(word2)) :
                ans += word1[i]
                ans += word2[i]
            ans += word1[len(word2):]
        
        return ans