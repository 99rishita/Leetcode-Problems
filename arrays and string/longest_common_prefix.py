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