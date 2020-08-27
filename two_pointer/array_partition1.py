class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            s = sorted(nums)
            sum1 = 0
            start = 0
            end = start+1
            while end <= len(nums)-1:
                sum1 += min(s[start], s[end])
                start = end+1
                end = start+1
            return sum1
        