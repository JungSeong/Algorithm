class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        l = []
        d = defaultdict(list)

        for i in range(len(strs)) :
            ch = "".join(sorted(strs[i]))
            d[ch].append(strs[i])
        
        answer = []

        for vals in d.values() :
            answer.append(vals)

        return answer