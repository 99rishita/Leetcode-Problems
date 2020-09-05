class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict_map = {}
        n = len(nums)
        for i in range(0, n):
            if nums[i] not in dict_map:
                dict_map[nums[i]] = 1
            elif nums[i] in dict_map:
                dict_map[nums[i]] += 1
                
        index = 0
        if 0 in dict_map:
            for i in range(dict_map[0]):
                nums[index] = 0
                index += 1
                
        if 1 in dict_map:
            for i in range(dict_map[1]):
                nums[index] = 1
                index += 1
                
        if 2 in dict_map:
            for i in range(dict_map[2]):
                nums[index] = 2
                index += 1