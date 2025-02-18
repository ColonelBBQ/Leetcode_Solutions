class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list(s.split())
        n = len(words)
        output = len(words[n-1])
        return output
