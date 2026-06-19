class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        good_pairs = 0
        for num in nums:
            if num in freq:
                good_pairs += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
        return good_pairs