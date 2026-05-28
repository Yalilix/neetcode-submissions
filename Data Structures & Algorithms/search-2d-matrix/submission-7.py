class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rowL, rowH = 0, len(matrix) - 1

        while rowL <= rowH:
            midRow = (rowL + rowH) // 2

            if matrix[midRow][0] > target:
                rowH = midRow - 1
            elif matrix[midRow][-1] < target:
                rowL = midRow + 1
            else:
                break
        
        midRow = (rowL + rowH) // 2
        colL, colH = 0, len(matrix[0]) - 1

        while colL <= colH:
            midCol = (colL + colH) // 2

            if matrix[midRow][midCol] > target:
                colH = midCol - 1
            elif matrix[midRow][midCol] < target:
                colL = midCol + 1
            else:
                return True

        return False