class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        h = {}
        for i, letter in enumerate(s):
            # when letter is present is dictionary and start is less than value of that character in hash map
            if letter in h and start <= h[s[i]]:
                start = h[s[i]] + 1
            # when letter is not present in map, just increase the maximum length
            else:
                max_length = max(max_length, i-start+1)
            #value for each character has to be updated irrespective of aboves 2 cases
            h[s[i]] = i
        return max_length
            