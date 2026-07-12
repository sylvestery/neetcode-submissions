class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left < right:
            mid = left + ( right -left) // 2
            r = mid // n
            c = mid % n
            curr = matrix[r][c]
            if target == curr:
                return True
            elif target > curr:
                left = mid + 1
            else: 
                right = mid

        
        return matrix[left // n][left%n] == target

        