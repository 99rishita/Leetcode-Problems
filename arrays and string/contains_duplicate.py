class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        dup_map = {}
        value_list = []
        for i in range(0, len(nums)):
            if nums[i] not in dup_map:
                dup_map[nums[i]] = 1
            elif nums[i] in dup_map:
                dup_map[nums[i]] += 1
                
        list1 = dup_map.values()
        print(list1)
        for i in list1:
            if i > 1:
                return True
        return False

--------------------------------------------------------------------------------------


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        dup_set = set()
        for i in nums:
            if i in dup_set:
                return True
            else:
                dup_set.add(i)
        return False