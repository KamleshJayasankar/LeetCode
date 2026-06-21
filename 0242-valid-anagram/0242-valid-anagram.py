class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = {}
        if len(s) != len(t):
            return False
        else:
            for c in s:
                if c in s_char:
                    s_char[c] += 1
                else:
                    s_char[c] = 1
            for c in t:
                if c in s_char:
                    s_char[c] -= 1 
                    if s_char[c] == 0:
                        del s_char[c]
                else:
                    return False
            if len(s_char) == 0:
                return True
            else:
                return False