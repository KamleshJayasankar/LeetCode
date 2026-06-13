class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_largest = nums[0]
        second_largest = None
        third_largest = None
        for i in range(1,len(nums)):
            if nums[i] > first_largest:
                if second_largest is None:
                    second_largest = first_largest
                    first_largest = nums[i]
                elif second_largest < first_largest and third_largest is None:
                    third_largest = second_largest
                    second_largest = first_largest
                    first_largest = nums[i]
                elif second_largest < first_largest and third_largest < second_largest:
                    third_largest = second_largest
                    second_largest = first_largest
                    first_largest = nums[i]
            elif first_largest > nums[i]:
                if second_largest is None:
                    second_largest = nums[i]
                elif second_largest < nums[i] and (third_largest is None or third_largest < second_largest):
                    third_largest = second_largest
                    second_largest = nums[i]
                #elif second_largest < nums[i] and third_largest < second_largest:
                #    third_largest = second_largest
                #    second_largest = nums[i]
                elif second_largest > nums[i] and (third_largest is None or third_largest < nums[i]):
                    third_largest = nums[i]
                #elif second_largest > nums[i] and third_largest < nums[i]:
                #    third_largest = nums[i]
        
        if third_largest is not None:
            return third_largest
        else:
            return first_largest