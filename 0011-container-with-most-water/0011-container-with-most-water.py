class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = []
        left, right = 0, len(height)-1

        while left < right :
            hl, hr = height[left], height[right]
            mh = hl if min(hl, hr) == hl else hr
            area.append(mh*(right-left))

            if mh == hl :
                left += 1
            else :
                right -= 1

        return max(area)