class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n
        for i in range(n-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)