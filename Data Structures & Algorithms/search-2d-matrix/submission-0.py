class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        print(m)
        print(n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==target:
                   return True
                else: 
                    continue
        return False
            