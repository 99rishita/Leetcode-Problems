class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t = 0
        while 0 in nums:
            for i, num in enumerate(nums):
                if nums[i] == 0:
                    nums.pop(i)
                    t += 1
        while(t):
            nums.append(0)
            t -= 1

------------------------------------------------------------------------------------

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t = 0
        count = 0
        count = nums.count(0)
        count2 = count
        while(count):
            nums.remove(0)
            count -= 1
        while(count2):
            nums.append(0)
            count2 -= 1

----------------------------------------------------------------------------------------

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[t] = nums[i]
                t += 1
                
        for i in range(t, len(nums)):
            nums[i] = 0