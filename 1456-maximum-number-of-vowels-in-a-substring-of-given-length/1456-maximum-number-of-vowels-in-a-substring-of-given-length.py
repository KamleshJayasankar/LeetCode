class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = s.lower()
        vowels = {'a','e','i','o','u'}
        current_count = 0
        for i in range(0,k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count
        for i in range(k,len(s)):
            if s[i] in vowels:
                current_count += 1
            if s[i-k] in vowels:
                current_count -= 1
            max_count = max(max_count,current_count)
        return max_count