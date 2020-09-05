class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = list(str(x))
        str1 = ''
        for i in range(len(num)-1, -1, -1):
            str1 += num[i]
        if str1 == str(x):
            return True
        else:
            return False