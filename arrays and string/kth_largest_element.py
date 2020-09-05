class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return sorted(nums)[-k]

#other solution with small change

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        return nums[n-k]
            