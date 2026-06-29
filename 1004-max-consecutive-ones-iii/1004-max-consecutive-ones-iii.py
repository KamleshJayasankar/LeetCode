class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        zc=0
        for j in nums:
            if j==0:
                zc+=1
            if zc>k:
                if nums[i]==0:
                    zc-=1
                i+=1
        return len(nums)-i