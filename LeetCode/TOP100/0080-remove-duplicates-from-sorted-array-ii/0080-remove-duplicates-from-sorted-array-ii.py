class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = [0]*len(nums)

        from collections import Counter
        cnt = Counter(nums)
        answer = 0

        for k, v in cnt.items() :
            if v >= 2 :
                v = 2
            for i in range(v) :
                arr[answer] = k
                answer += 1

        nums[:] = arr
        return answer