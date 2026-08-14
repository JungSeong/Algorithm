class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from collections import defaultdict
        alphabet = defaultdict(list)

        for i in range(26) :
            if 15<=i<=18 :
                idx = 7
            elif 19<=i<=21 :
                idx = 8
            elif 22<=i<=25 :
                idx = 9
            else :
                idx = i//3+2
            ch = chr(ord('a')+i)

            alphabet[str(idx)].append(ch)

        lists = []

        from itertools import product
        for ch in digits :
            lists.append(alphabet[ch])

        answer = []
        for comb in list(product(*lists)) :
            answer.append(''.join(comb))

        return answer