class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        row = (top + bottom) // 2
        l, h = 0, len(matrix[row]) - 1

        while l <= h:
            m = (l + h) // 2
            if matrix[row][m] > target:
                h = m - 1 
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False

