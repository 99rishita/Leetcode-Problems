class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        max_val = 0
        banned_set = set(banned)
        #make all characters lowercase and replace other punctuation marks with space
        collection = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = collection.split()
        paragraph_map = {}
        for word in words:
            if word not in banned_set and word not in paragraph_map:
                paragraph_map[word] = 1
            elif word in paragraph_map:
                paragraph_map[word] += 1
        values_list = list(paragraph_map.values())
        keys_list = list(paragraph_map.keys())
        max_val = max(values_list)
        index_val = values_list.index(max_val)
        find_key = keys_list[index_val]
        return find_key