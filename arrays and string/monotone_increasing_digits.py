class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N
        num = list(str(N))
        i = 1
        while i < len(num) and num[i-1] <= num[i]:
            i += 1
        while 0 < i < len(num) and num[i-1] > num[i]:
            num[i-1] = str(int(num[i-1])-1)
            i -= 1
        num[i+1:] = '9'*(len(num)-i-1)
        return int(''.join(num))