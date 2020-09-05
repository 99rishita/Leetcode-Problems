class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i+j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
                    d[i+j].append(matrix[i][j])
                    
        ans = []
        
        for key, val in d.items():
            if key % 2 == 0:
                [ans.append(v) for v in val[::-1]]
            else:
                [ans.append(v) for v in val]
                
        return ans