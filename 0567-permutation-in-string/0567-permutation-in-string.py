class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        seen_s1 = {}
        seen_s2 = {}
        for char in s1:
            if char in seen_s1:
                seen_s1[char] += 1
            else:
                seen_s1[char] = 1
        for i in range(0,len(s1)):
            if s2[i] in seen_s2:
                seen_s2[s2[i]] += 1
            else:
                seen_s2[s2[i]] = 1
        if seen_s1 == seen_s2:
            return True
        for i in range(len(s1),len(s2)):
            if s2[i] in seen_s2:
                seen_s2[s2[i]] += 1
            else:
                seen_s2[s2[i]] = 1
            leaving = s2[i-len(s1)]
            seen_s2[leaving] -= 1
            if seen_s2[leaving] == 0:
                del seen_s2[leaving]
            if seen_s1 == seen_s2:
                return True
        return False
