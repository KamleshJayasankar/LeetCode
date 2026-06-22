class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}
        for i in magazine:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i in ransomNote:
            if i in seen:
                seen[i] -= 1
                if seen[i] == 0:
                    del seen[i]
            else:
                return False
        return True