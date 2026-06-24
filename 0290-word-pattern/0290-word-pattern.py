class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(word) != len(pattern):
            return False
        map_pw = {}
        map_wp = {}
        for i in range(0,len(pattern)):
            if pattern[i] in map_pw:
                if map_pw[pattern[i]] != word[i]:
                    return False
            else:
                map_pw[pattern[i]] = word[i]
        for i in range(0,len(word)):
            if word[i] in map_wp:
                if map_wp[word[i]] != pattern[i]:
                    return False
            else:
                map_wp[word[i]] = pattern[i]
        return True