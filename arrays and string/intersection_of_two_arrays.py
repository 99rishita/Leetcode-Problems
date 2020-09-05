class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_map1 = {}
        list1 = []
        n = len(nums1)
        m = len(nums2)
        if m >= n:
            for i in range(0, n):
                if nums1[i] in nums2 and nums1[i] not in dict_map1:
                    dict_map1[nums1[i]] = 1
                    #list1.append(nums1[i])
                    nums2.remove(nums1[i])
                elif nums1[i] in nums2 and nums1[i] in dict_map1:
                    dict_map1[nums1[i]] += 1
                    #list1.append(nums1[i])
                    nums2.remove(nums1[i])
                
        elif n > m:
            for i in range(0, m):
                if nums2[i] in nums1 and nums2[i] not in dict_map1:
                    dict_map1[nums2[i]] = 1
                    #list1.append(nums2[i])
                    nums1.remove(nums2[i])
                elif nums2[i] in nums1 and nums2[i] in dict_map1:
                    dict_map1[nums2[i]] += 1
                    #list1.append(nums2[i])
                    nums1.remove(nums2[i])
            
        for key, val in dict_map1.items():
            while(val != 0):
                list1.append(key)
                val -= 1
                    
        
        return list1

