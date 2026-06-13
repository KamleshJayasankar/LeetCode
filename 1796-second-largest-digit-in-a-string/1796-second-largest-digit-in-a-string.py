class Solution:
    def secondHighest(self, s: str) -> int:
        nums = []
        for i in s:
            if i.isdigit():
                nums.append(int(i))
        if len(nums) > 0:
            first = nums[0]
            second = None
            for i in range(1,len(nums)):
                if nums[i] > first:
                    second = first
                    first = nums[i]
                elif nums[i] != first and second is None:
                    second = nums[i]
                elif nums[i] != first and second < nums[i]:
                    second = nums[i]
        
            if second is not None:
                return second
            else:
                return -1
        else:
            return -1