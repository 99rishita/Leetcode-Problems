class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dup_set = {}
        for i in range(0, len(nums)):
            if nums[i] not in dup_set:
                dup_set[nums[i]] = 1
            elif nums[i] in dup_set:
                dup_set[nums[i]] += 1
                
        for key, val in dup_set.items():
            if val == 1:
                return key