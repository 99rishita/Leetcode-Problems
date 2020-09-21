class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = []
        right = []
        prod_l, prod_r = 1, 1
        prod = 1
        for i in range(len(nums)):
            prod_l = prod_l * nums[i]
            left.append(prod_l)
            
        for i in range(len(nums)-1, -1, -1):
            prod_r = prod_r * nums[i]
            right.append(prod_r)
        right = right[::-1]
            
        res.append(right[1])
        for i in range(1, len(nums)-1):
            prod = left[i-1]*right[i+1]
            res.append(prod)
        res.append(left[len(nums)-2])
        
        return res
            
        