nums = [4,3,2,7,8,2,3,1]
res = []
for i in range(len(nums)):
    pos = abs(nums[i])
    if nums[pos-1] < 0:
        continue
    k = (-1)*nums[pos-1]
    print(k, end=" ")
    nums[pos-1] = k
print(nums)
    
for i in range(len(nums)):
    k = nums[i]
    if k > 0:
        res.append(i+1)
        
print(res)