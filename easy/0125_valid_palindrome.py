class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = ''.join(char for char in s.lower() if char.isalnum())
        s_clean_reverersed = s_clean[::-1]

        return s_clean == s_clean_reverersed
