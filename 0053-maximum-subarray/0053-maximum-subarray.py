class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = nums[0]
        for n in nums[1:]:
            curSum = max(curSum + n , n)
            maxSub = max(maxSub,curSum)
        return maxSub