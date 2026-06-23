class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_st = {}
        map_ts = {}
        for i in range(0,len(s)):
            if s[i] in map_st:
                if map_st[s[i]] != t[i]:
                    return False
            else:
                map_st[s[i]] = t[i]
            if t[i] in map_ts:
                if map_ts[t[i]] != s[i]:
                    return False
            else:
                map_ts[t[i]] = s[i]
        return True