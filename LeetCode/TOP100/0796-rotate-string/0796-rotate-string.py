class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        length = len(s)

        for i in range(length-1, -1, -1) :
            if s == goal :
                return True
            s = s[1:] + s[0]
        
        return False