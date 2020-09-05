class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(0, len(nums)):
            h[nums[i]] = i
        for j in range(0, len(nums)):
            check_num = target - nums[j]
            if check_num in h and h[check_num] != j:
                return [h[check_num], j]