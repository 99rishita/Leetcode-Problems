class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_map = {}
        index_val = 0
        if s == "":
            return -1
        for i in range(0, len(s)):
            if s[i] not in string_map:
                string_map[s[i]] = 1
            elif s[i] in string_map:
                string_map[s[i]] += 1
        for key, val in string_map.items():
            if val == 1:
                index_val = s.index(key)
                return index_val
        return -1