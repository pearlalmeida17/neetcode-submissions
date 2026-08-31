class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        target_row = -1

        while top <= bottom:

            mid_row = (top + bottom) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                target_row = mid_row 
                break
            
        if target_row == -1:
            return False
        

        l, r = 0, cols - 1
        
        while l <= r:
            mid = (l + r )// 2

            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False



        