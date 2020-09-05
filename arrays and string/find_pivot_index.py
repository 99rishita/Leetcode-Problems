class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        leftsum = 0
        for i in range(0, len(nums)):
            rightsum = s-nums[i]-leftsum
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1