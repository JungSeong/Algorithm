class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        cr, cm = Counter(ransomNote), Counter(magazine)

        for k, v in cr.items() :
            if k not in cm :
                return False
            else :
                if v > cm[k] :
                    return False
        
        return True