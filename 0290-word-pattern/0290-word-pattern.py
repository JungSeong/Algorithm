class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = dict()
        l = s.split()

        if len(pattern) != len(l) :
            return False

        for i in range(len(pattern)) :
            if pattern[i] not in d :
                if l[i] in d.values() :
                    return False
                d[pattern[i]] = l[i]
            else :
                if d[pattern[i]] != l[i] :
                    return False

        return True