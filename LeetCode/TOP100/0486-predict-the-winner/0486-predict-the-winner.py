class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def Predict(num1, num2, start, end, before) :
            if start > end :
                if num1 >= num2 :
                    return True
                return False
            answer = False
            if before == 2 :
                return (Predict(num1+nums[start], num2, start+1, end, 1) or Predict(num1+nums[end], num2, start, end-1, 1))
            else :
                return (Predict(num1, num2+nums[start], start+1, end, 2) and Predict(num1, num2+nums[end], start, end-1, 2))

        return Predict(0, 0, 0, len(nums)-1, 2)