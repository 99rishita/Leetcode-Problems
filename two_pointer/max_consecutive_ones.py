class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        max_count = 0
        i = j = 0
        while i < len(nums):
            j = i+1
            count = 0
            while j <= (len(nums)-1) and nums[i] == nums[j] and nums[i] == 1:
                j += 1
                count += 1
            i = j
            max_count = max(max_count, count)
            if j == len(nums)-1:
                break
        return max_count+1