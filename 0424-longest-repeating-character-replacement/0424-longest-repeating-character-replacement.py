class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        right = 0
        max_length =0
        while right < len(s):
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
            while (right-left+1)-max(seen.values()) > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            max_length = max(max_length, right-left+1)
            right += 1
        return max_length