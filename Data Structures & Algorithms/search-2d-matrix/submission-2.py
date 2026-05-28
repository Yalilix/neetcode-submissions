class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lorow, hirow = 0, rows - 1

        while lorow <= hirow:
            midrow = (hirow + lorow) // 2
            if target > matrix[midrow][-1]:
                lorow = midrow + 1
            elif target < matrix[midrow][0]:
                hirow = midrow - 1
            else: 
                break

        if not (lorow <= hirow):
            return False
        
        l, r = 0, cols - 1
        row = (hirow + lorow) // 2
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False