class Solution:
    def isHappy(self, n: int) -> bool:
        
        def findSum(n):
            s = 0
            rem = 0
            while n>0:
                rem = n%10
                s += (rem**2)
                n = n//10
            return s
        
        seen = set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = findSum(n)
        
        return n==1
                