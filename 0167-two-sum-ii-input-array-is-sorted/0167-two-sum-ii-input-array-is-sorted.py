class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while (left < right):
            result = numbers[left] + numbers[right]
            if (result == target):
                num1 = left+1
                num2 = right+1
                return (num1 , num2)
            elif(target > result):
                left += 1
            else:
                right -= 1
        