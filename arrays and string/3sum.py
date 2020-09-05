class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp_array = []
        seen = {}
        found = set()
        dup = set()
        for i, val1 in enumerate(nums):
            if val1 not in dup:
                dup.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1-val2
                    if complement in seen and seen[complement] == i:
                        min_value = min(val1,val2,complement)
                        max_value = max(val1,val2,complement)
                        if (min_value, max_value) not in found:
                            found.add((min_value, max_value))
                            temp_array.append([val1,val2,complement])
                    seen[val2] = i
        return temp_array