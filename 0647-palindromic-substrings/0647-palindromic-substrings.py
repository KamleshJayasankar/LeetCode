class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def count_palindromes(left: int, right: int) -> int:
            p_count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                p_count += 1
                left -= 1
                right += 1
            return p_count

        for i in range(len(s)):
            count += count_palindromes(i, i)
            count += count_palindromes(i, i + 1)

        return count