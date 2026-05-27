class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        from collections import defaultdict
        s, S = defaultdict(list), defaultdict(list)
        cnt = 0
        
        for i in range(len(word)) :
            if word[i].islower() :
                s[word[i]].append(i)
            else :
                ch = chr(ord(word[i])-ord('A')+ord('a'))
                S[ch].append(i)

        for k, v in s.items() :
            if k in S.keys() :
                isOK = True
                for val in v :
                    if val >= S[k][0] :
                        isOK = False
                        break
                
                if isOK :
                    cnt += 1

        return cnt