class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""

        indices = [i for i, ch in enumerate(s) if ch == "1"]

        best_substring = ""
        min_len = float("inf")

        for i in range(len(indices) - k + 1):
            start = indices[i]
            end = indices[i + k - 1]
            sub = s[start : end + 1]
            curr_len = end - start + 1

            if curr_len < min_len:
                min_len = curr_len
                best_substring = sub
            elif curr_len == min_len:
                best_substring = min(best_substring, sub)

        return best_substring