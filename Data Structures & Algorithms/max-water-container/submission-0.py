class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left = 0
        right = n-1
        maxArea = 0
        while left < right:
            area = (right - left) * (min(heights[left], heights[right]))
            maxArea = max(maxArea, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return maxArea
        