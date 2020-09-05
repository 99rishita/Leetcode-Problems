import re
class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.lstrip() #left strip to remove whitespaces
        regex = "[/+/-]?[0-9]+"
        words = re.findall(regex, s)

        if len(words) == 0:
            return 0

        if not s[0].isnumeric():
            if s[0] is not in ['+','-'] or not s[1].isnumeric():
                return 0

        # number should be in range of INT_MAX(2^31 - 1) and INT_MIN(-(2^31))
        return min(max(int(words[0]), -(2**31)), 2**31 - 1)