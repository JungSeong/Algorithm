from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        unique = set()
        
        for k, v in cnt.items() :
            if v == 1 :
                unique.add(k)
                
        for i in range(len(s)) :
            if s[i] in unique :
                return i
        
        return -1