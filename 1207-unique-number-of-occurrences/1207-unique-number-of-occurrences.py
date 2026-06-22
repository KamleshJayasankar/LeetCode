class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        seen = set()
        for num in freq:
            if freq[num] in seen:
                return False
            else:
                seen.add(freq[num])
        return True
