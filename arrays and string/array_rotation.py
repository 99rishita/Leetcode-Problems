nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
nums = nums[n-k:]+nums[:k+1]
print(nums)