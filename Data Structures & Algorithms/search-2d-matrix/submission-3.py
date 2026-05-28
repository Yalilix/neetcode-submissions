class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerL, outerH = 0, len(matrix) - 1
        targetRow = -1

        while outerL <= outerH:
            outerMid = (outerL + outerH) // 2
            if target > matrix[outerMid][-1]:
                outerL = outerMid + 1
            elif target < matrix[outerMid][0]:
                outerH = outerMid - 1
            else:
                targetRow = outerMid
                break

        l, h = 0, len(matrix[targetRow]) - 1

        while l <= h:
            m = (l + h) // 2
            if target > matrix[targetRow][m]:
                l = m + 1
            elif target < matrix[targetRow][m]:
                h = m - 1
            else:
                return True
        return False
