class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if nums == [] or nums == []:
            return 0
        
        nums.sort()
        res = 0
        for i in range(len(nums)):
            check = target - nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] < check:
                    res += right-left
                    left += 1
                else:
                    right -= 1
        return res