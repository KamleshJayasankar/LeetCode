class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*(2*n)
        for i in range(0,len(ans)):
            if i < n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-n]
        return ans