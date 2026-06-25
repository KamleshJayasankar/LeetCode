class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_slide = sum(nums[0:k])
        max_sum = window_slide
        for i in range(k,len(nums)):
            window_slide = window_slide + nums[i] - nums[i-k]
            max_sum = max(max_sum , window_slide)

        return max_sum / k