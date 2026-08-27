from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_count = Counter(s)

        def get_remaining_sorted(counts):
            res = []
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if counts[ch] > 0:
                    res.append(ch * counts[ch])
            return "".join(res)

        prefix_counts = []
        curr_counts = Counter(s)
        match_len = 0

        for i in range(n):
            prefix_counts.append(curr_counts.copy())
            if curr_counts[target[i]] > 0:
                curr_counts[target[i]] -= 1
                match_len += 1
            else:
                break

        for i in range(min(match_len, n - 1), -1, -1):
            counts = prefix_counts[i]
            target_char = target[i]

            for o in range(ord(target_char) + 1, ord("z") + 1):
                c = chr(o)
                if counts[c] > 0:
                    counts_copy = counts.copy()
                    counts_copy[c] -= 1
                    ans = target[:i] + c + get_remaining_sorted(counts_copy)
                    return ans

        return ""