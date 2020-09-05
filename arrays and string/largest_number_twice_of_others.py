class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        largest_index = nums.index(largest)
        nums.sort()
        for i in range(len(nums)):
            if i == len(nums)-1:
                return largest_index
            if largest >= 2*nums[i]:
                continue
            else:
                return -1