class Solution:
    def climbStairs(self, n):
        count = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 2
        result = 0
        for i in range(3, n+1):
            result = first+second
            first = second
            second = result
        return result