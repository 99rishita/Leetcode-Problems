from collections import defaultdict 
def group(strs):
    ans = defaultdict(list)
    for i in strs:
        print(i)
        s = tuple(sorted(i))
        #ans[s] = i 
        #this is not done, since assigning replaces the value in key:value pair and doesn't add value in list
        ans[s].append(i)
    print(ans)

        
        



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
group(strs)