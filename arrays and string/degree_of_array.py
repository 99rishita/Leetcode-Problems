class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1
                
        degree = max(h.values())
        if degree == 1:
            return 1
        else:
            min_len = len(nums)
            for keys in h:
                j = len(nums)-1
                if h[keys] == degree:
                    pos1 = nums.index(keys)
                    while j > 0:
                        if nums[j] == keys:
                            break
                        j -= 1
                    pos2 = j
                    d = pos2-pos1+1
                    min_len = min(d,min_len)
                
        return min_len