class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(needle) == 1 and len(haystack) == 1:
            return 0
        h, n = len(haystack), len(needle)
        for i in range(h-n+1):
            if haystack[i:n+i] == needle:
                return i
        return -1