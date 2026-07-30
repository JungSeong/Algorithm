class Solution:
    def minimumPushes(self, word: str) -> int:
        p, q = len(word)//8, len(word)%8
        answer = 0

        for i in range(1, p+1) :
            answer += i*8
        answer += (p+1)*q
        return answer