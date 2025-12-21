class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_len = 0

        while left < right:
            cal_area = min(height[left] , height[right]) * (right-left)
            max_len = max(max_len , cal_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_len