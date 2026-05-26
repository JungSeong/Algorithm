class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []
        length = len(nums)

        for i in range(length-3) :
            for j in range(i+1, length-2) :
                s, e = j+1, len(nums)-1
                while s < e :
                    total = nums[i] + nums[j] + nums[s] + nums[e]
                    if total == target :
                        ans = [nums[i], nums[j], nums[s], nums[e]]
                        if len(answer)!=0 and ans not in answer :
                            answer.append(ans)
                        if len(answer) == 0 :
                            answer.append(ans)
                        s += 1
                        e -= 1
                    elif total < target :
                        s += 1
                    else :
                        e -= 1

        return answer