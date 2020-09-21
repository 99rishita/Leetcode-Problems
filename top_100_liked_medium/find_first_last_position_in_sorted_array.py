class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ind = 0
        if target in nums:
            first = nums.index(target)
            ind = first+1
            while(ind < len(nums)):
                if target == nums[ind]:
                    ind += 1
                else:
                    break
            last = ind-1
            return [first,last]
        else:
            return [-1,-1]