def trapping(height):
    sumtotal = 0
    h = len(height)
    
    for i in range(0, h-1):
        for j in range(i+1, h):
            if height[i] > height[j]:
                sumtotal += height[i] - height[j]
            break
    return sumtotal

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping(height))
