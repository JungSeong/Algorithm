class Solution:
    def isValid(self, s: str) -> bool:
        answer = []

        for ch in s :
            if ch in ['(', '[', '{'] :
                answer.append(ch)
            else :
                if answer :
                    if answer[-1] == '(' and ch == ")" :
                        answer.pop()
                    elif answer[-1] == '[' and ch == "]" :
                        answer.pop()
                    elif answer[-1] == '{' and ch == "}" :
                        answer.pop()
                    else :
                        return False
                else :
                    return False

        print(answer)
        
        if answer :
            return False
        else :
            return True