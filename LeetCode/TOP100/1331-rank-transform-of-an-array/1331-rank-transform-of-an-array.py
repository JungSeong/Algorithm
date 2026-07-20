class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        carr = arr[:]
        carr.sort()

        d = dict()
        rank = 1

        for i in range(len(carr)) :
            if i>0 and carr[i-1] != carr[i] :
                rank += 1
            d[carr[i]] = rank

        answer = []
        for i in range(len(arr)) :
            answer.append(d[arr[i]])

        return answer