class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
            
        def recursionSum(c, combination, target, pos):
            if target == 0:
                result.append(combination+[])
                return

            for i in range(pos, len(c)):
                if target < c[i]:
                    break
                combination.append(c[i])
                recursionSum(c, combination, target-c[i], i)
                combination.pop()

        recursionSum(sorted(candidates), [], target, 0)
        return result
            