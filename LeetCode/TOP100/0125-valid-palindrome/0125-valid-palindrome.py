class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        answer = []

        for ch in s :
            ch = ch.lower()
            if ch.isalpha() or ch.isdigit() :
                answer.append(ch)

        s = "".join(answer)

        if s == s[::-1] :
            return True
        else :
            return False