def find_subset(arr, subset, index):
    #print(*subset)
    for i in range(index, len(arr)):
        subset.append(arr[i])

        find_subset(arr, subset, i+1)

        subset.pop(-1)
    if subset != []:
        print(subset)

arr = [1,2,3]
subset = []
index = 0
find_subset(arr, subset, index)