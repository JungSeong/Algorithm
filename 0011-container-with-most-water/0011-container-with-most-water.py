class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = []
        left, right = 0, len(height)-1

        while left < right :
            mh = height[left] if min(height[left], height[right]) == height[left] else height[right]
            area.append(mh*(right-left))

            if mh == height[left] :
                left += 1
            else :
                right -= 1

        return max(area)