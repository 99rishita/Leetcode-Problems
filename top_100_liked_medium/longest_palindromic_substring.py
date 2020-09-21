class Solution:
    def longestPalindrome(self, s: str) -> str:
        str1 = str2 = ''
        ans_str = ''
        max_len = 0
        for i in range(0, len(s)):
            for j in range(len(s)-1, i-1, -1):
                if s[i] == s[j]:
                    str1 = s[i:j+1]
                    if len(str1) < len(ans_str):
                        break
                    str2 = str1[::-1]
                    if str1 == str2 and len(str1) > max_len:
                        max_len = max(max_len,len(str1))
                        ans_str = str1
                        
        return ans_str