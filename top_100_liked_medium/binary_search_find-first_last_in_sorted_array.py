class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        result.append(self.binary_search_left(nums, target))
        result.append(self.binary_search_right(nums, target))
        return result
        
        
    def binary_search_left(self, nums, target):
        index = -1
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] >= target:
                end = mid-1
            else:
                start = mid+1
            if target == nums[mid]:
                index = mid
        return index
                
    def binary_search_right(self, nums, target):
        index = -1
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if target >= nums[mid]:
                start = mid+1
            else:
                end = mid-1
            if target == nums[mid]:
                index = mid
        return index