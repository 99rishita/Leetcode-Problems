b = [3,4,5,5,6]
a = [3,4,5]
res = []
i = 0 
j = 0
if len(a) > len(b):
	while j < len(b):
		if a[i] > b[j]:
			j += 1
		elif a[i] < b[j]:
			i += 1
		elif a[i] == b[j]:
			res.append(b[j])	
			i += 1
			j += 1
		if j == len(b):
			print(res)
else:
	while j < len(a):
		if b[i] > a[j]:
			j += 1
		elif b[i] < a[j]:
			i += 1
		elif b[i] == a[j]:
			res.append(a[j])	
			i += 1
			j += 1
		if j == len(a):
			print(res)