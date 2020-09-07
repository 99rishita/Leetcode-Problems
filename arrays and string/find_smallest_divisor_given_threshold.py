from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)+1
        res = 0
        
        def checksum(m):
            sum1 = 0
            for i in nums:
                sum1 += ceil(i/m)
            return sum1 <= threshold
        
        while l < r:
            mid = (l+r)//2
            if checksum(mid):
                res = mid
                r = mid
            else:
                l = mid+1
                
        return res
                
                