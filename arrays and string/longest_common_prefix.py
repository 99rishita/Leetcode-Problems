def longestCommonPrefix(strs):
    str1 = ''
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    strs = sorted(strs)
    print(strs)
    for s in strs[0]:
        print(s)
        if strs[-1].startswith(str1+s):
            str1 += s
        else:
            break
    print(str1)

strs = ['flower', 'flow', 'flight']
longestCommonPrefix(strs)


-----------------------------------------------------------------------------------------------------------------------------


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        str1 = ""
        lst = sorted(strs)
        i = 0
        first, last = lst[0], lst[-1]
        f_len, l_len = len(first), len(last)
        l = min(f_len, l_len)
        while i < l and first[i] == last[i]:
            str1 += first[i]
            i += 1
        return str1
        