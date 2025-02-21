class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        x_reverse = ''
        for item in reversed(x_list):
            x_reverse += item

        if str(x_reverse) == str(x):
            return True

        else:
            return False
