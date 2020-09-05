class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {'(':')', '{':'}', '[':']'}
        open_brackets = set(['(', '{', '['])
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif stack and i == brackets_map[stack[-1]]:
                stack.pop()
            else:
                return False
        if stack == []:
            return True