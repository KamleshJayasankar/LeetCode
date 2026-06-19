class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit = 0
        for num in nums:
            current = 0
            while num > 0:
                current += 1
                num = num//10
            if current%2 == 0:
                even_digit += 1
        return even_digit