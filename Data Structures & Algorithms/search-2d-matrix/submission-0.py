import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = np.array(matrix)
        arr = arr.reshape(-1)
        n = len(arr)
        l, r = 0, n-1

        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
        
        return False