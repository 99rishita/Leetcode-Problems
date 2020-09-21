class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod_l, product = 1,1 
        for i in range(len(nums)):
            prod_l = prod_l*nums[i]
            res.append(prod_l)
            
        for i in range(len(nums)-1, 0, -1):
            res[i] = res[i-1]*product
            product = product*nums[i]
        res[0] = product
        return res
        