class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        start = 0

        for end in range(n + 1):

            if end == n or chars[end] == " ":
                left, right = start, end - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                start = end + 1

        return "".join(chars)