class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            # Quick response for empty matrix
            return []
        ans = []
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        size = len(matrix) * len(matrix[0])
        while True:
            #moving left to right
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            
            #moving top to bottom
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            
            #moving right to left
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            
            #moving bottom to top
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
            
        return ans
                
                
        