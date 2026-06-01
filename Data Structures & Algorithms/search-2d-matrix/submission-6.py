class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix[0]) <= 1 and matrix[0][0] == target:
                return True
        for row in matrix:
            l = 0
            r = len(matrix[0]) - 1 
            mid = (l + r) // 2
            if target == row[mid]:
                return True
            while l <= r:
                print(row[mid])
                if row[mid] < target:
                    l = mid + 1
                elif row[mid] > target:
                    r = mid - 1
                elif target == row[mid]:
                    return True
                mid = (l+r) // 2
        return False

            
            


