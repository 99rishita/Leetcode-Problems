class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            op_ind = nums.index(target)
            return op_ind
        ind = 0
        while(target > nums[ind] and ind < len(nums)):
            ind += 1
            if ind == len(nums):
                break
        return ind