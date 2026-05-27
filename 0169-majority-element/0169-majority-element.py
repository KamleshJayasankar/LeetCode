class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        found = {}
        for num in nums:
            if num in found:
                found[num] += 1
            else:
                found[num] = 1
        for num,count in found.items():
            if count > len(nums)//2:
                return num