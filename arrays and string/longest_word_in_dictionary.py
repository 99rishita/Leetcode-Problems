class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ""
        res = set()
        res.add("")
        
        for word in words:
            if word[:-1] in res:#check if prefix is present in the set or not
                if len(word) > len(ans):
                    ans = word
                res.add(word) #Add Prefix in res set
        return ans