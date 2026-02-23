class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        left , right = 0 , len(cleaned)-1
        while(left < right):
            if cleaned[left] == cleaned[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
