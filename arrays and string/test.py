def quicksort(arr, first, last):
	if first < last:
		r = partition(arr, first, last)

		quicksort(arr, first, r-1)
		quicksort(arr, r+1, last)

	
def partition(arr, first, last):
	pivot = arr[last]
	i = first-1
	for j in range(first, last+1):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	return i


arr = [9,4,6,3,7,1,2,11,5]
first = 0
last = len(arr)-1
quicksort(arr, first, last)
print(arr)




