class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find row that contains range of the target
        # check rightmost value of row, if it is bigger than the target
        #we check the eftmost value of the same row, if its within that range
        #than the value is within that row, if its smaller than we shift bottom pointer
        #to the middle and vise versa for if the target is larger then the
        #mid value until we find the correct range

        top, bottom = 0, len(matrix) - 1 #lets find for this one first
        l, r = 0, len(matrix[0]) -1
        mid_row = (top + bottom) // 2
        target_row = None

        while top <= bottom:
            if matrix[mid_row][-1] < target:
                top = mid_row + 1
            elif matrix[mid_row][0] > target:
                bottom = mid_row - 1
            elif matrix[mid_row][0] == target or matrix[mid_row][-1] == target:
                return True
            else:
                target_row = matrix[mid_row]
                break
            mid_row = (top + bottom) // 2
        print(matrix[mid_row])
        print(top)
        print(bottom)
        # if we go thorugh the entire row, and our pointers dont match, 
        #then we knwo that the range of 
        #values in the matrix dont contain the target value antways so we return fasle
        if top > bottom: 
            return False

        mid_col = (l + r) // 2 # mid target initally
        print(mid_col)
        print(target_row)
        while l <= r:
            if target_row[mid_col] == target:
                return True
            if target_row[mid_col] < target:
                l = mid_col + 1
            elif target_row[mid_col] > target:
                r = mid_col - 1
            mid_col = (l + r) // 2
        return False
            





        
        

