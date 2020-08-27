class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(numbers)):
            if numbers[i] not in h:
                h[numbers[i]] = i
            elif numbers[i] in h:
                h[numbers[i]] = i
        for i in range(len(numbers)):
            check = abs(target-numbers[i])
            ind = numbers.index(numbers[i])
            if check in h and h[check]!=ind:
                return [ind+1, h[check]+1]
        