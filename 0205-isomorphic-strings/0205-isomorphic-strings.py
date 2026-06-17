class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        for i in range(len(s)) :
            ch = s[i]
            if ch not in d :
                if t[i] not in d.values() :
                    d[ch] = t[i]
                else :
                    return False
            else :
                if d[ch] == t[i] :
                    continue
                else :
                    return False

        return True